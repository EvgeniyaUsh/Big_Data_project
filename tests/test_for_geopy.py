import pytest
from weather_analysis.app.geo_py import get_geo

list_coordinates = ['40.91089, -111.40339', '42.183544, -122.663345']

expected_result = ['Coalville, Summit County, Utah, United States of America'
                   'Clover Lane, Ashland, Jackson County, Oregon, 95520, United States of America']


# tests for big_data_project/geo_py
@pytest.mark.parametrize(
    ["list_of_coordinates", "api_key", "max_work", "expected_result"],
    [
        (list_coordinates, 'api_key', 8, expected_result),
    ],
)
def test_get_address_by_geo_coordinates(list_of_coordinates, api_key, max_work, expected_result):
    actual_result = get_geo(list_of_coordinates, api_key, max_work)['Address'].values
    assert actual_result == expected_result
