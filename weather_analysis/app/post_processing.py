import pandas as pd


def get_day_and_city_with_max_temperature(max_temperature: dict, path: str):
    """
    Функция находит город и день с максимальной температурой за рассматриваемый период и сохраняет
    полученную информацию в csv формате;
    :param max_temperature: словарь с максимальными температурами для каждого дня за рассматриваемый период
    :return:
    """
    df = pd.DataFrame(max_temperature)
    city_with_max_temperature = df.max()[df.max() == df.max(axis=1).max()].index  # axis=0 - строки, axis=1 - колонки
    data_max_temperature = df.idxmax()[city_with_max_temperature][0]

    city, country = city_with_max_temperature[0][1], city_with_max_temperature[0][0]

    data = [[data_max_temperature, city_with_max_temperature[0][1]]]
    df = pd.DataFrame(data, columns=['Data', 'Temperature'])
    df.to_csv(f'{path}/{country}/{city}/day_and_city_with_max_temperature.csv', index=False)


def get_city_with_max_change_in_max_temperature(max_temperature: dict, path: str):
    """
    Функция находит город с максимальным изменением максимальной температуры за рассматриваемый период и сохраняет
    полученную информацию в csv формате;
    :param max_temperature: словарь с максимальными температурами для каждого дня за рассматриваемый период
    :return:
    """
    df = pd.DataFrame(max_temperature)
    max_temp = df.max()
    min_temp = df.min()
    temp_difference = max_temp - min_temp
    city_with_max_difference = temp_difference.idxmax()[1]
    country = temp_difference.idxmax()[0]

    data = pd.DataFrame([city_with_max_difference], columns=['City'], index=None)
    data.to_csv(f'{path}/{country}/{city_with_max_difference}/city_with_max_change_in_max_temperature.csv', index=False)


def get_day_and_city_with_min_temperature(min_temperature: dict, path: str):
    """
    Функция находит город и день наблюдения с минимальной температурой за рассматриваемый период и сохраняет
    полученную информацию в csv формате;
    :param min_temperature: словарь с минимальными температурами для каждого дня за рассматриваемый период
    :return:
    """
    df = pd.DataFrame(min_temperature)
    city_with_min_temperature = df.min()[df.min() == df.min(axis=1).min()].index
    data_min_temperature = df.idxmin()[city_with_min_temperature][0]

    city, country = city_with_min_temperature[0][1], city_with_min_temperature[0][0]

    data = [[city_with_min_temperature[0][1], data_min_temperature]]
    df = pd.DataFrame(data, columns=['Data', 'City'], index=None)
    df.to_csv(f'{path}/{country}/{city}/day_and_city_with_min_temperature.csv', index=False)


def get_day_and_city_with_max_difference_between_max_min_temp(max_temperature: dict, min_temperature: dict, path: str):
    """
    Функция находит город и день с максимальной разницей между максимальной и минимальной температурой за
    рассматриваемый период и сохраняет полученную информацию в csv формате;
    :param max_temperature: словарь с максимальными температурами для каждого дня за рассматриваемый период
    :param min_temperature: словарь с минимальными температурами для каждого дня за рассматриваемый период
    :return:
    """
    df_with_max_temp = pd.DataFrame(max_temperature)
    df_with_min_temp = pd.DataFrame(min_temperature)
    df_with_difference_temp = df_with_max_temp - df_with_min_temp
    city_with_max_difference_temp = df_with_difference_temp.max()[
        df_with_difference_temp.max() == df_with_difference_temp.max(axis=1).max()].index
    data_max_difference_temp = df_with_difference_temp.idxmax()[city_with_max_difference_temp][0]

    city, country = city_with_max_difference_temp[0][1], city_with_max_difference_temp[0][0]

    data = [[data_max_difference_temp, city_with_max_difference_temp[0][1]]]
    df = pd.DataFrame(data, columns=['Data', 'City'], index=None)
    df.to_csv(f'{path}/{country}/{city}/day_and_city_with_max_difference_between_max_min_temp.csv', index=False)
