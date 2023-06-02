"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture()
def item_iphone():
    return Item("Iphone", 50000, 20)


#Testcase#1 Calculate_total_price
def test_calculate_total_price(item_iphone):
    assert item_iphone.calculate_total_price() == 1000000


#Testcase#2 Apply_discount
def test_apply_discount(item_iphone):
    item_iphone.apply_discount()
    assert item_iphone.price == 40000


#Testcase#3 Item.__name.getter
def test_name_getter(item_iphone):
    assert item_iphone.name == 'Iphone'


#Testcase#4 Item.__name.setter
def test_name_setter(item_iphone, new_name='Samsung'):
    item_iphone.name = new_name
    assert item_iphone.name == new_name


def test_name_setter1(item_iphone, new_name='Samsung Galaxy'):
    item_iphone.name = new_name
    assert item_iphone.name != new_name


#Testcase#5 String_to_number
def test_string_to_number():
    assert Item.string_to_number('6') == 6
    assert Item.string_to_number('10.0') == 10

