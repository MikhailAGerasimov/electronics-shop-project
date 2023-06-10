import csv, pathlib


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    @property
    def name(self):
        """
        Getter для __name
        """
        return self.__name

    @name.setter
    def name(self, new_name):
        """
        Setter для __name и проверка на длину названия(мение 10 символов)
        """
        if len(new_name) <= 10:
            self.__name = new_name
        else:
            print("Exception: Длина наименования товара превышает 10 символов.")

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.quantity * self.price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @staticmethod
    def string_to_number(number: str):
        """
        Statcimethod: ковертирует строку в целое число
        """
        return int(float(number))

    @classmethod
    def instantiate_from_csv(cls):
        """
        Classmethod: загружает список товаров из CSV файла и создает экземплры класса на каждый товар
        """
        path = pathlib.Path(__file__).parent.parent / 'src' / 'items.csv'
        cls.all.clear()
        with open(path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Item(row['name'], row['price'], row['quantity'])
