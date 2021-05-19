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
    piv = df.pivot_table(index=['City'], columns=['Country'], values='Name', aggfunc='count', fill_value=0)
    dict_for_count_hotels = {}
    for i in piv:
        dict_for_count_hotels[i] = piv[i].idxmax()

    df = df.loc[df['City'].isin(dict_for_count_hotels.values())]

    df.reset_index(drop=True, inplace=True)
    return df


if __name__ == '__main__':
    unpack_zip('data/hotels.zip')
    df = create_dataframe_from_csv_files('output_folder')
    df = clearing_data(df)
    df = get_cities_with_max_numbers_of_hotel(df)
    print(df)
