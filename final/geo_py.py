import concurrent
from geopy import OpenMapQuest
from geopy.extra.rate_limiter import RateLimiter
from typing import List


# получение адресов отелей по координатам в многопоточном режиме
def get_geo(list_of_coordinates: List[str], api_key: str) -> dict:
    geolocator = OpenMapQuest(api_key=api_key)
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1 / 20)

    with concurrent.futures.ThreadPoolExecutor() as e:
        locations = dict(e.map(geocode, list_of_coordinates))
    return locations
