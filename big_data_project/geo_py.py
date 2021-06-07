from concurrent.futures import ThreadPoolExecutor
from geopy import OpenMapQuest
from geopy.extra.rate_limiter import RateLimiter
from typing import List
import pandas as pd


def get_geo(list_of_coordinates: List[str], api_key: str, max_work: int) -> pd.DataFrame:
    """
    Функция получает адреса по координатам в многопоточном режиме
    :param max_work: количество потоков для параллельной обработки данных
    :param list_of_coordinates: список с координатами
    :param api_key: API ключ для OpenMapQuest
    :return df: dataframe с адресом и координатами
    """
    geolocator = OpenMapQuest(api_key=api_key)
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1 / 20)

    with ThreadPoolExecutor(max_workers=max_work) as e:
        locations = dict(e.map(geocode, list_of_coordinates))

    # словарь с координатами и адресом преобразуется в DataFrame
    df = pd.DataFrame(locations.values(), index=locations.keys(),
                      columns=['Latitude', 'Longitude'])
    df['Address'] = df.index
    df = df.reset_index(drop=True)
    return df
