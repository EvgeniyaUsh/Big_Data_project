import csv
import math
import zipfile
import click as click
import pandas as pd
import glob
from temperatures import get_temperature
import os
from geo_py import get_geo
from plotting import build_a_graph_with_max_temperature, build_a_graph_with_min_temperature
from post_processing import get_day_and_city_with_max_temperature, get_day_and_city_with_min_temperature, \
    get_city_with_max_change_in_max_temperature, get_day_and_city_with_max_difference_between_max_min_temp


def unpack_zip(path: str):
    """
    Функция распаковывет zip архив и помещает распакованные файлы в директорию csv_files_for_work
    :param path: путь до zip архива
    """
    z = zipfile.ZipFile(path, 'r')
    z.extractall('csv_files_for_work')


def create_dataframe_from_csv_files(path: str) -> pd.DataFrame:
    """
    Функция создает dataframe из распакованных csv файлов
    :param path: путь где лежат csv файлы
    :return dataframe: dataframe из распакованных csv файлов
    """
    folder_name = path
    file_type = 'csv'
    seperator = ','
    dataframe = pd.concat(
        [pd.read_csv(f, sep=seperator, encoding='utf-8') for f in glob.glob(folder_name + "/*." + file_type)],
        ignore_index=True)
    return dataframe


def clearing_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Функция очищает данные от невалидных записей (содержащих заведомо ложные значения или отсутствующие необходимые элементы)
    :param df: dataframe из распакованных csv файлов
    :return df: валидный dataframe
    """
    df = df.dropna(axis=0)  # удаление отсутствующих элементов.
    k = []
    for i, j in df.iterrows():
        try:
            if (90 >= float(j['Latitude']) >= -90) == False or (180 >= float(j['Longitude']) >= -180) == False:
                k.append(i)
        except ValueError:
            k.append(i)

    df = df.drop(k)  # удаляет строки по индексам
    df.reset_index(drop=True, inplace=True)  # меняет индексы на новые упорядоченные, старые удаляет
    return df


def get_cities_with_max_numbers_of_hotel(df: pd.DataFrame) -> pd.DataFrame:
    """
    Функция создает dataframe, который содержить только те города, в которых больше всего отелей в стране
    :param df: валидный dataframe
    :return df: отсортированный dataframe с городами в которых больше всего отелей в стране
    """
    df_cities = df.groupby(['Country', 'City'], as_index=False).agg({'Name': 'count'}).sort_values('Country') \
        .sort_values('Name', ascending=False).drop_duplicates('Country')
    df_cities['Location'] = df_cities[['Country', 'City']].apply(tuple, axis=1)
    df['Location'] = df[['Country', 'City']].apply(tuple, axis=1)
    df = df.loc[df['Location'].isin(df_cities['Location'])]
    df.reset_index(drop=True, inplace=True)
    return df


def get_centre_coordinates(df: pd.DataFrame) -> dict:
    """
    Функция находит центры координат для каждого города с максимальным количеством отелей
    :param df: dataframe с городами в которых больше всего отелей в стране
    :return: dict с центральными координатами для каждой локации
    """
    df = df.astype({'Latitude': float})
    df = df.astype({'Longitude': float})
    df = df.groupby(['Location'], as_index=False).agg({'Latitude': 'mean', 'Longitude': 'mean'})
    dict_from_df = (df.set_index('Location').T.to_dict('list'))  # создается словарь из df c ключами-локациями
    return dict_from_df


def concat_str(x, y):
    """
    Функция для конкатинации двух строк
    :param x:
    :param y:
    :return: x, y
    """
    return x + ", " + y


def get_list_with_coordinates(df: pd.DataFrame) -> list:
    """
    Функция преобразует dataframe в список строк с координатами Latitude, Longitude
    :param df: dataframe с городами в которых больше всего отелей в стране
    :return list: список с координатами в виде: ['Latitude, Longitude']
    """
    df = df[['Latitude', 'Longitude']]
    df = df.astype({'Latitude': str})
    df = df.astype({'Longitude': str})
    df['Coordinates'] = [concat_str(x, y) for x, y in zip(df.Latitude.values, df.Longitude.values)]
    list_with_coordinates = [i for i in df['Coordinates']]
    return list_with_coordinates


def get_dataframe_with_address_and_write_csv(df1, df2, path: str):
    """
    Функция проеобразует два dataframe в dataframe состоящий из столбцов (Name, Address, Latitude, Longitude)
    и сохраняет в csv формат данные по каждой стране и городу отдельно
    :param df1: dataframe с городами в которых больше всего отелей в стране
    :param df2: dataframe с адресами и геокоординатами
    :return:
    """
    df = df1.combine_first(df2)
    df = df.dropna(axis=0)
    loc = df['Location'].unique()
    for i in loc:
        country, city = i
        new_path = f'{path}/{country}/{city}'
        data = df.loc[df['Location'] == i]
        data.reset_index(drop=True, inplace=True)
        del data['Location']
        del data['City']
        del data['Country']
        save_dataframe_in_csv(data, new_path)


def save_dataframe_in_csv(df: pd.DataFrame, path: str):
    """
    Функция сохраняет DataFrame в csv файлы содержащие не более 100 записей в каждом;
    :param df: DataFrame для сохранения в csv формат
    :param path: путь, куда будет сохранен полученный csv файл
    :return:
    """
    number_of_splits = math.ceil(len(df) / 100)
    os.makedirs(f"{path}", exist_ok=True)
    file_opens = [open(f"{path}/address_latitude_longitude_name_hotels_data{i}.csv", "w") for i in
                  range(number_of_splits)]
    file_writers = [csv.writer(v, lineterminator='\n') for v in file_opens]
    for i, row in df.iterrows():
        file_writers[math.floor((i / df.shape[0]) * number_of_splits)].writerow(row.tolist())
    for file in file_opens:
        file.close()


@click.command()
@click.argument('input_path')  # data/hotels.zip
@click.argument('output_path')  # output_folder
@click.argument('max_workers')
@click.argument('api_key_weather')  # e25c6ede689bcfda9998c67a52b0612a
@click.argument('api_key_geo')  # GPm29mRy2v4JMGHGdtAxbOcyakPfFGVy
def main(input_path, output_path, max_workers, api_key_weather, api_key_geo):
    """
    Утилита предназначена для многопоточной обработки данных,
    аккумулирования результатов через API из Интернета и их дальнейшего представления на графиках.
    Утилита принимает на вход входные и выходные каталоги, число потоков для многопоточной обработки
    и 2 API-ключа.
    Все полученные результаты будут располагаться в выходном каталоге со следующей структурой
    {output_folder}\{country}\{city}\.
    Пример использования:
    C:/data/input_folder C:/data/output_folder Кол-во_потоков Ваш_API-OpenWeatherMap Ваш_API-OpenMapQuest
    Для использования приложения Вам необходимы 2 API-ключа.
    1й-для работы с OpenWeatherMap. Вы можете зарегистрировать бесплатный
    аккаунт на https://openweathermap.org/appid.
    2й-для работы с OpenMapQuest. Вы можете зарегистрировать бесплатный
    аккаунт на https://developer.mapquest.com/
    """
    unpack_zip(input_path)
    df = create_dataframe_from_csv_files('csv_files_for_work')
    print('Файлы распакованы')
    df = clearing_data(df)
    df = get_cities_with_max_numbers_of_hotel(df)
    list_with_coordinates = get_list_with_coordinates(df)

    df_with_lon_lat_address = get_geo(list_with_coordinates, api_key_geo, int(max_workers))
    get_dataframe_with_address_and_write_csv(df, df_with_lon_lat_address, output_path)
    print('Адреса получены')

    dict_with_centre_of_coordinates = get_centre_coordinates(df)
    min_temperature, max_temperature = get_temperature(dict_with_centre_of_coordinates, api_key_weather)
    print('Температуры для каждого дня получена')

    build_a_graph_with_min_temperature(min_temperature, output_path)
    build_a_graph_with_max_temperature(max_temperature, output_path)
    print('Графики построены и сохранены')

    get_day_and_city_with_max_temperature(max_temperature, output_path)
    get_city_with_max_change_in_max_temperature(max_temperature, output_path)
    get_day_and_city_with_min_temperature(min_temperature, output_path)
    get_day_and_city_with_max_difference_between_max_min_temp(max_temperature, min_temperature, output_path)

    print(f"Утилита отработала успешно. Данные сохранены в {output_path}/")


if __name__ == '__main__':
    main()
