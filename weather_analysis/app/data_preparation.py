

def unpack_zip(path: str):
    """
    Функция распаковывет zip архив и помещает распакованные файлы в директорию csv_files_for_work
    :param path: путь до zip архива
    """
    z = zipfile.ZipFile(path, 'r')
    z.extractall('csv_files_for_work')


def create_dataframe_from_csv_files(path: str) -> pd.DataFrame:
    """
    Функция создает dataframe из распакованных csv файлов
    :param path: путь где лежат csv файлы
    :return dataframe: dataframe из распакованных csv файлов
    """
    folder_name = path
    file_type = 'csv'
    seperator = ','
    dataframe = pd.concat(
        [pd.read_csv(f, sep=seperator, encoding='utf-8') for f in glob.glob(folder_name + "/*." + file_type)],
        ignore_index=True)
    return dataframe


def clearing_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Функция очищает данные от невалидных записей
    (содержащих заведомо ложные значения или отсутствующие необходимые элементы)
    :param df: dataframe из распакованных csv файлов
    :return df: валидный dataframe
    """
    df = df.dropna(axis=0)  # удаление отсутствующих элементов.
    k = []
    for i, j in df.iterrows():
        try:
            if not (90 >= float(j['Latitude']) >= -90) or not (180 >= float(j['Longitude']) >= -180):
                k.append(i)
        except ValueError:
            k.append(i)

    df = df.drop(k)  # удаляет строки по индексам
    df.reset_index(drop=True, inplace=True)  # меняет индексы на новые упорядоченные, старые удаляет
    return df