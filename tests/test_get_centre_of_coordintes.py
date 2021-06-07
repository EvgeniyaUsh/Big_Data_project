import pytest
from weather_analysis.app.data_processing import get_centre_coordinates
import pandas as pd

df = pd.read_csv('file_for_get_centre_of_coordinates.csv', delimiter=',')
expected_dict = {'Milan': [45.48280116, 9.19175882]}


# tests for weather_analysis/app/get_centre_coordinates.py
@pytest.mark.parametrize(
    ["df", "expected_result"],
    [
        (df, expected_dict),
    ],
)
def test_get_centre_of_coordinates(df, expected_result):
    actual_result = get_centre_coordinates(df)
    assert actual_result == expected_result
