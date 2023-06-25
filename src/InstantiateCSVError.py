import csv, pathlib


class FileNotFoundError(Exception):
    def __init__(self):
        print('_Отсутствует файл item.csv_')

class InstantiateCSVError(Exception):
    def __init__(self):
        print('_Файл item.csv поврежден_')