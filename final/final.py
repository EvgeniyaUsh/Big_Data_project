import zipfile
import pandas as pd
import glob
from temeratures import get_temperature
import matplotlib.pyplot as plt
import seaborn as sns
import os


def unpack_zip(path: str):
    z = zipfile.ZipFile(path, 'r')
    z.extractall('csv_files_for_work')


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


def get_centre_coordinates(df):
    df = df.astype({'Latitude': float})
    df = df.astype({'Longitude': float})
    df = df.groupby(['Location'], as_index=False).agg({'Latitude': 'mean', 'Longitude': 'mean'})
    df = (df.set_index('Location').T.to_dict('list'))
    return df


def build_a_graph_with_min_temperature(min_temperarutes: dict):
    df_min_temperatures = pd.DataFrame(min_temperarutes)
    for i in df_min_temperatures:
        country, city = i
        ax = sns.lineplot(x=df_min_temperatures.index, y=df_min_temperatures[i])
        plt.xticks(rotation=45)
        ax.set_title('Min Temperature', fontsize=15)
        ax.set_xlabel("t'C", fontsize=14)
        ax.set_ylabel("Data", fontsize=14)
        fig = ax.get_figure()
        os.makedirs(f"output_folder/{country}/{city}")
        fig.savefig(f"output_folder/{country}/{city}/min_temperature_in_{i}.png")
        plt.clf()


def build_a_graph_with_max_temperature(max_temperarutes: dict):
    df_max_temperatures = pd.DataFrame(max_temperarutes)
    for i in df_max_temperatures:
        country, city = i
        ax = sns.lineplot(x=df_max_temperatures.index, y=df_max_temperatures[i])
        plt.xticks(rotation=45)
        ax.set_title('Max Temperature', fontsize=15)
        ax.set_xlabel("t'C", fontsize=14)
        ax.set_ylabel("Data", fontsize=14)
        fig = ax.get_figure()
        fig.savefig(f"output_folder/{country}/{city}/max_temperature_in_{i}.png")
        plt.clf()


if __name__ == '__main__':
    unpack_zip('data/hotels.zip')
    df = create_dataframe_from_csv_files('csv_files_for_work')
    df = clearing_data(df)
    df = get_cities_with_max_numbers_of_hotel(df)
    df = get_centre_coordinates(df)
    temperarutes = get_temperature(df, 'api_key')
    min_temperarutes, max_temperarutes = temperarutes
    build_a_graph_with_min_temperature(min_temperarutes)
    build_a_graph_with_max_temperature(max_temperarutes)
