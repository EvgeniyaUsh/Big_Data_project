import pytest
from weather_analysis.app.data_processing import get_list_with_coordinates
import pandas as pd

df = pd.read_csv('file_for_get_coordinates.csv', delimiter=',')
expected_list = ['40.91089, -111.40339',
                 '42.183544, -122.663345',
                 '43.45161, -76.53235',
                 '49.802514, 9.921491']


# tests for weather_analysis/app/get_list_with_coordinates.py
@pytest.mark.parametrize(
    ["df", "expected_result"],
    [
        (df, expected_list),
    ],
)
def test_get_list_with_coordinates(df, expected_result):
    actual_result = get_list_with_coordinates(df)
    assert actual_result == expected_result
