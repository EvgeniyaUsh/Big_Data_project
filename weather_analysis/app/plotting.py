import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


def build_a_graph_with_min_temperature(min_temperature: dict, path: str):
    """
    Функция строит графики минимальной температуры, с зависимостью от даты
    :param min_temperature: словарь с ключами-датами и минимальными температурами
    :param path: путь для сохранения графиков
    """
    df_min_temperatures = pd.DataFrame(min_temperature)
    for i in df_min_temperatures:
        country, city = i
        ax = sns.lineplot(x=df_min_temperatures.index, y=df_min_temperatures[i])
        plt.xticks(rotation=45)
        ax.set_title('Min Temperature', fontsize=15)
        ax.set_xlabel("t'C", fontsize=14)
        ax.set_ylabel("Data", fontsize=14)
        fig = ax.get_figure()
        os.makedirs(f"{path}/{country}/{city}", exist_ok=True)
        fig.savefig(f"{path}/{country}/{city}/min_temperature_in_{i}.png")
        plt.clf()


def build_a_graph_with_max_temperature(max_temperature: dict, path: str):
    """
     Функция строит графики максимальной температуры, с зависимостью от даты
     :param max_temperature:  словарь с ключами-датами и макимальными температурами
     :param path: путь для сохранения графиков
     """
    df_max_temperatures = pd.DataFrame(max_temperature)
    for i in df_max_temperatures:
        country, city = i
        ax = sns.lineplot(x=df_max_temperatures.index, y=df_max_temperatures[i])
        plt.xticks(rotation=45)
        ax.set_title('Max Temperature', fontsize=15)
        ax.set_xlabel("t'C", fontsize=14)
        ax.set_ylabel("Data", fontsize=14)
        fig = ax.get_figure()
        fig.savefig(f"{path}/{country}/{city}/max_temperature_in_{i}.png")
        plt.clf()
