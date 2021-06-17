import pandas as pd
from printError import printErr


def csvReader(filename: str, delimiter: str = ','):
    name_list = filename.split('.')
    if name_list[-1] != 'csv':
        raise NameError('File name not compatible')
    try:
        pd.read_csv(filename, delimiter)
    except FileNotFoundError as err:
        printErr(err, 3)
