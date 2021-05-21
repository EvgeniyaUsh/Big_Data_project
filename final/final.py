# df.columns: Index(['Id', 'Name', 'Country', 'City', 'Latitude', 'Longitude'], dtype='object')
import zipfile
import pandas as pd
import glob


def unpack_zip(path: str):
    z = zipfile.ZipFile(path, 'r')
    z.extractall('output_folder')


def create_dataframe_from_csv_files(path: str):
    folder_name = path
    file_type = 'csv'
    seperator = ','
    dataframe = pd.concat(
        [pd.read_csv(f, sep=seperator, encoding='utf-8') for f in glob.glob(folder_name + "/*." + file_type)],
        ignore_index=True)
    return dataframe


def clearing_data(df: pd.DataFrame):
    df = df.dropna(axis=0)  # Country и City чистится полносью с помощью этой функции
    del df['Id']
    k = []
    for i, j in df.iterrows():
        try:
            if (90 >= float(j['Latitude']) >= -90) == False or (180 >= float(j['Longitude']) >= -180) == False:
                k.append(i)
        except ValueError:
            k.append(i)

    df = df.drop(k)  # 2378
    df.reset_index(drop=True, inplace=True)  # меняет индексы на новые упорядоченные, старые удаляет, не делает копию df
    return df


#  dataframe который содержить только те города, в которых больше всего отелей в стране
def get_cities_with_max_numbers_of_hotel(df: pd.DataFrame):
    df_cities = df.groupby(['Country', 'City'], as_index=False).agg({'Name': 'count'}).sort_values('Country') \
        .sort_values('Name', ascending=False).drop_duplicates('Country')
    df_cities['Location'] = df_cities[['Country', 'City']].apply(tuple, axis=1)
    df['Location'] = df[['Country', 'City']].apply(tuple, axis=1)
    df = df.loc[df['Location'].isin(df_cities['Location'])]
    df.reset_index(drop=True, inplace=True)
    return df


def get_max_min_coordinates(df):
    df = df.astype({'Latitude': float})
    df = df.astype({'Longitude': float})

    max_coordinates = df.groupby(['Location'], as_index=False).agg(
        {'Latitude': 'max', 'Longitude': 'max'}).rename(
        columns={'Latitude': 'Latitude_max', 'Longitude': 'Longitude_max'})  # максимальные значения координат

    min_coordinates = df.groupby(['Location'], as_index=False).agg(
        {'Latitude': 'min', 'Longitude': 'min'}).rename(
        columns={'Latitude': 'Latitude_min', 'Longitude': 'Longitude_min'})  # минимальные значения координат

    min_max_df = max_coordinates.merge(min_coordinates, on='Location')

    return min_max_df


if __name__ == '__main__':
    unpack_zip('data/hotels.zip')
    df = create_dataframe_from_csv_files('output_folder')
    df = clearing_data(df)
    df = get_cities_with_max_numbers_of_hotel(df)
    df = get_max_min_coordinates(df)
    print(df)
