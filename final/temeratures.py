import requests
from datetime import date, timedelta, datetime
import time


# ошибка на 5 дней {'message': 'requested time is out of allowed range of 5 days back'}


# функция для получения температуры (текущей/5 следующих дней/4 предыдущих дня) по координатам
def get_temperature(city_with_coordinates: dict, api_key: str) -> dict:
    one_day_ago = date.today() - timedelta(1)
    one_day_ago_ = int(time.mktime(one_day_ago.timetuple()))

    two_days_ago = date.today() - timedelta(days=2)
    two_days_ago_ = int(time.mktime(two_days_ago.timetuple()))

    three_days_ago = date.today() - timedelta(days=3)
    three_days_ago_ = int(time.mktime(three_days_ago.timetuple()))

    four_days_ago = date.today() - timedelta(days=4)
    four_days_ago_ = int(time.mktime(four_days_ago.timetuple()))

    app_id = api_key

    temperature_in_kelvin = {}

    for k, v in city_with_coordinates.items():
        lat = v[0]
        lon = v[1]
        today = requests.get('https://api.openweathermap.org/data/2.5/onecall',
                             params={'lat': lat, 'lon': lon, 'appid': app_id, 'units': 'metric'})
        previous_1_day = requests.get('https://api.openweathermap.org/data/2.5/onecall/timemachine',
                                      params={'lat': lat, 'lon': lon, 'appid': app_id, 'dt': one_day_ago_,
                                              'units': 'metric'})
        previous_2_days = requests.get('https://api.openweathermap.org/data/2.5/onecall/timemachine',
                                       params={'lat': lat, 'lon': lon, 'appid': app_id, 'dt': two_days_ago_,
                                               'units': 'metric'})
        previous_3_days = requests.get('https://api.openweathermap.org/data/2.5/onecall/timemachine',
                                       params={'lat': lat, 'lon': lon, 'appid': app_id, 'dt': three_days_ago_,
                                               'units': 'metric'})
        previous_4_days = requests.get('https://api.openweathermap.org/data/2.5/onecall/timemachine',
                                       params={'lat': lat, 'lon': lon, 'appid': app_id, 'dt': four_days_ago_,
                                               'units': 'metric'})
        next_day = requests.get('https://api.openweathermap.org/data/2.5/onecall',
                                params={'lat': lat, 'lon': lon, 'appid': app_id,
                                        'units': 'metric'})

        data_now = today.json()
        data_1_day_ago = previous_1_day.json()
        data_2_days_ago = previous_2_days.json()
        data_3_days_ago = previous_3_days.json()
        data_4_days_ago = previous_4_days.json()
        data_next = next_day.json()

        temperature_in_kelvin[k] = {date.today().strftime('%Y-%m-%d'): data_now['current']['temp'],
                                    one_day_ago.strftime('%Y-%m-%d'): data_1_day_ago['current']['temp'],
                                    two_days_ago.strftime('%Y-%m-%d'): data_2_days_ago['current']['temp'],
                                    three_days_ago.strftime('%Y-%m-%d'): data_3_days_ago['current']['temp'],
                                    four_days_ago.strftime('%Y-%m-%d'): data_4_days_ago['current']['temp'],
                                    datetime.utcfromtimestamp(data_next['daily'][1:6][0]['dt']).strftime('%Y-%m-%d')
                                    : data_next['daily'][1:6][0]['temp']['day'],
                                    datetime.utcfromtimestamp(data_next['daily'][1:6][1]['dt']).strftime('%Y-%m-%d')
                                    : data_next['daily'][1:6][1]['temp']['day'],
                                    datetime.utcfromtimestamp(data_next['daily'][1:6][2]['dt']).strftime('%Y-%m-%d')
                                    : data_next['daily'][1:6][2]['temp']['day'],
                                    datetime.utcfromtimestamp(data_next['daily'][1:6][3]['dt']).strftime('%Y-%m-%d')
                                    : data_next['daily'][1:6][3]['temp']['day'],
                                    datetime.utcfromtimestamp(data_next['daily'][1:6][4]['dt']).strftime('%Y-%m-%d')
                                    : data_next['daily'][1:6][4]['temp']['day'],
                                    }

    return temperature_in_kelvin



