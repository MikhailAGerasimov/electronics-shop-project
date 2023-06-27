import csv, pathlib


class FileNotFoundError(Exception):
    def __init__(self):
        self.message = "_Отсутствует файл item.csv_"

    def __str__(self):
        return self.message

class InstantiateCSVError(Exception):
    def __init__(self):
        self.message = "_Файл item.csv поврежден_"

    def __str__(self):
        return self.message