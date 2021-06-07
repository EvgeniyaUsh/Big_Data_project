import pandas as pd


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
