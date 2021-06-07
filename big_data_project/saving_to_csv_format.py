import csv
import pandas as pd


def get_dataframe_with_address_and_write_csv(df1: pd.DataFrame, df2: pd.DataFrame, path: str):
    """
    Функция проеобразует два dataframe в dataframe состоящий из столбцов (Name, Address, Latitude, Longitude)
    и сохраняет в csv формат данные по каждой стране и городу отдельно
    :param path: путь к директории для сохранения полученных файлов
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
        file_writers[math.int((i / df.shape[0]) * number_of_splits)].writerow(row.tolist())
    for file in file_opens:
        file.close()
