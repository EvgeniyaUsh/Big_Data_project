import asyncio
import zipfile
import csv
from multiprocessing import Pool
from geopy.exc import GeocoderTimedOut
from geopy.extra.rate_limiter import RateLimiter
from geopy.adapters import AioHTTPAdapter
from geopy.extra.rate_limiter import AsyncRateLimiter
import geopy
import pandas as pd
import numpy as np
import glob
from geopy.geocoders import Nominatim

z = zipfile.ZipFile('data/hotels.zip', 'r')

z.extractall('output_folder')

folder_name = 'output_folder'
file_type = 'csv'
seperator = ','
dataframe = pd.concat(
    [pd.read_csv(f, sep=seperator, encoding='utf-8') for f in glob.glob(folder_name + "/*." + file_type)],
    ignore_index=True)
# df = dataframe.replace(['', 0.0], np.nan)
df = dataframe.dropna(axis=0)  # Country и City чистится полносью с помощью этой функции

# df.columns: Index(['Id', 'Name', 'Country', 'City', 'Latitude', 'Longitude'], dtype='object')


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

# таблица с количеством отелей в каждом городе страны
piv = df.pivot_table(index=['City'], columns=['Country'], values='Name', aggfunc='count', fill_value=0)

dict_for_count_hotels = {}
for i in piv:
    dict_for_count_hotels[i] = piv[i].idxmax()

df = df.loc[df['City'].isin(dict_for_count_hotels.values())]

#  dataframe который содержить только те города, в которых больше всего отелей в стране
df.reset_index(drop=True, inplace=True)

dict_for_coordinates = {}

for i, j in df.iterrows():
    dict_for_coordinates[j['Name']] = f'{j["Latitude"]}, {j["Longitude"]}'

list_points = list(dict_for_coordinates.values())  # список координат


# получение адреса по координатам, НЕ РАБОТАЕТ!
async def get_geo():
    async with Nominatim(
            user_agent="Name",
            adapter_factory=AioHTTPAdapter,
    ) as geolocator:
        search = list_points
        try:
            reverse = AsyncRateLimiter(geolocator.reverse, min_delay_seconds=1)
            locations = [await reverse(s) for s in search]
            print(locations)
            raise GeocoderTimedOut
        except GeocoderTimedOut as e:
            print('pass', e)


# еще одно получение адреса по координатам, ТОЖЕ НЕ РАБОТАЕТ!
"""
geolocator = Nominatim(user_agent='Name')
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

with concurrent.futures.ThreadPoolExecutor() as e:
    locations = list(e.map(geocode, list_points))

"""


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_geo())
    loop.close()


if __name__ == '__main__':
    main()
