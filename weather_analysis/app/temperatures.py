import requests
from datetime import date, timedelta, datetime
import time


def get_temperature(city_with_coordinates: dict, api_key: str) -> dict:
    """
    Функция получает максимальные и минимальные температуры на текущий день/5 следующих дней/4 предыдущих дня
    по координатам, через API сайта https://api.openweathermap.org/
    :param city_with_coordinates: словарь с городами и их координатами
    :param api_key: API ключ сайта https://api.openweathermap.org/
    :return min_temperature_in_kelvin, max_temperature_in_kelvin:
    словари с минимальными и максимальными температурами за текущий день/5 следующих дней/4 предыдущих дня
    """
    one_day_ago = date.today() - timedelta(1)
    one_day_ago_ = int(time.mktime(one_day_ago.timetuple()))

    two_days_ago = date.today() - timedelta(days=2)
    two_days_ago_ = int(time.mktime(two_days_ago.timetuple()))

    three_days_ago = date.today() - timedelta(days=3)
    three_days_ago_ = int(time.mktime(three_days_ago.timetuple()))

    four_days_ago = date.today() - timedelta(days=4)
    four_days_ago_ = int(time.mktime(four_days_ago.timetuple()))

    app_id = api_key

    min_temperature_in_kelvin = {}
    max_temperature_in_kelvin = {}

    url_weather = 'https://api.openweathermap.org/data/2.5/onecall'

    for k, v in city_with_coordinates.items():
        lat = v[0]
        lon = v[1]

        params = {'lat': lat, 'lon': lon, 'appid': app_id, 'units': 'metric'}

        try:
            if requests.get(url_weather, params=params):
                current_and_forecast_weather = requests.get(url_weather, params=params)
                previous_1_day = requests.get(f'{url_weather}/timemachine',
                                              params={**params, **{'dt': one_day_ago_}})
                previous_2_days = requests.get(f'{url_weather}/timemachine',
                                               params={**params, **{'dt': two_days_ago_}})
                previous_3_days = requests.get(f'{url_weather}/timemachine',
                                               params={**params, **{'dt': three_days_ago_}})
                previous_4_days = requests.get(f'{url_weather}/timemachine',
                                               params={**params, **{'dt': four_days_ago_}})

                current_and_forecast_data = current_and_forecast_weather.json()
                data_1_day_ago = previous_1_day.json()
                data_2_days_ago = previous_2_days.json()
                data_3_days_ago = previous_3_days.json()
                data_4_days_ago = previous_4_days.json()

                min_temperature_in_kelvin[k] = {
                    date.today().strftime('%Y-%m-%d'): current_and_forecast_data['daily'][0]['temp']['min'],
                    one_day_ago.strftime('%Y-%m-%d'): min(
                        [i['temp'] for i in data_1_day_ago['hourly']]),
                    two_days_ago.strftime('%Y-%m-%d'): min(
                        [i['temp'] for i in data_2_days_ago['hourly']]),
                    three_days_ago.strftime('%Y-%m-%d'): min(
                        [i['temp'] for i in data_3_days_ago['hourly']]),
                    four_days_ago.strftime('%Y-%m-%d'): min(
                        [i['temp'] for i in data_4_days_ago['hourly']]),
                    datetime.utcfromtimestamp(current_and_forecast_data['daily'][1:6][0]['dt']).strftime(
                        '%Y-%m-%d'): current_and_forecast_data['daily'][1:6][0]['temp']['min'],
                    datetime.utcfromtimestamp(current_and_forecast_data['daily'][1:6][1]['dt']).strftime(
                        '%Y-%m-%d'): current_and_forecast_data['daily'][1:6][1]['temp']['min'],
                    datetime.utcfromtimestamp(current_and_forecast_data['daily'][1:6][2]['dt']).strftime(
                        '%Y-%m-%d'): current_and_forecast_data['daily'][1:6][2]['temp']['min'],
                    datetime.utcfromtimestamp(current_and_forecast_data['daily'][1:6][3]['dt']).strftime(
                        '%Y-%m-%d'): current_and_forecast_data['daily'][1:6][3]['temp']['min'],
                    datetime.utcfromtimestamp(current_and_forecast_data['daily'][1:6][4]['dt']).strftime(
                        '%Y-%m-%d'): current_and_forecast_data['daily'][1:6][4]['temp']['min'],
                }

                max_temperature_in_kelvin[k] = {
                    date.today().strftime('%Y-%m-%d'): current_and_forecast_data['daily'][0]['temp']['max'],
                    one_day_ago.strftime('%Y-%m-%d'): max(
                        [i['temp'] for i in data_1_day_ago['hourly']]),
                    two_days_ago.strftime('%Y-%m-%d'): max(
                        [i['temp'] for i in data_2_days_ago['hourly']]),
                    three_days_ago.strftime('%Y-%m-%d'): max(
                        [i['temp'] for i in data_3_days_ago['hourly']]),
                    four_days_ago.strftime('%Y-%m-%d'): max(
                        [i['temp'] for i in data_4_days_ago['hourly']]),
                    datetime.utcfromtimestamp(current_and_forecast_data['daily'][1:6][0]['dt']).strftime(
                        '%Y-%m-%d'): current_and_forecast_data['daily'][1:6][0]['temp']['max'],
                    datetime.utcfromtimestamp(current_and_forecast_data['daily'][1:6][1]['dt']).strftime(
                        '%Y-%m-%d'): current_and_forecast_data['daily'][1:6][1]['temp']['max'],
                    datetime.utcfromtimestamp(current_and_forecast_data['daily'][1:6][2]['dt']).strftime(
                        '%Y-%m-%d'): current_and_forecast_data['daily'][1:6][2]['temp']['max'],
                    datetime.utcfromtimestamp(current_and_forecast_data['daily'][1:6][3]['dt']).strftime(
                        '%Y-%m-%d'): current_and_forecast_data['daily'][1:6][3]['temp']['max'],
                    datetime.utcfromtimestamp(current_and_forecast_data['daily'][1:6][4]['dt']).strftime(
                        '%Y-%m-%d'): current_and_forecast_data['daily'][1:6][4]['temp']['max'],
                }
        except requests.exceptions.RequestException as ex:
            print(f'Error {ex}')

    return min_temperature_in_kelvin, max_temperature_in_kelvin
