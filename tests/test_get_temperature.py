from unittest.mock import patch

import weather_analysis.app.temperatures

expected_dicts = ({'Milan': {'2021-06-07': 17.34, '2021-06-06': 17.87, '2021-06-05': 16.6, '2021-06-04': 16.35,
                             '2021-06-03': 15.36, '2021-06-08': 17.37, '2021-06-09': 17.68, '2021-06-10': 18.04,
                             '2021-06-11': 17.51, '2021-06-12': 18.87}}, {
                      'Milan': {'2021-06-07': 26.28, '2021-06-06': 26.67, '2021-06-05': 29.32, '2021-06-04': 27.8,
                                '2021-06-03': 24.92, '2021-06-08': 27.1, '2021-06-09': 26.97, '2021-06-10': 28.51,
                                '2021-06-11': 27.17, '2021-06-12': 29.41}})


# tests for weather_analysis/app/temperatures/get_temperature.py via mock/patch
def test_get_weather_from_openweathermap():
    with patch(
            "weather_analysis.app.temperatures.get_temperature") as f:
        f.return_value = expected_dicts
        assert weather_analysis.app.temperatures.get_temperature({'Milan': [45.4642651, 9.1960569]},
                                                                 'api_key') == expected_dicts
