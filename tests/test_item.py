"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

@pytest.fixture()
def item_iphone():
    return Item("Iphone", 50000, 20)

def test_calculate_total_price(item_iphone):
    assert item_iphone.calculate_total_price() == 1000000


def test_apply_discount(item_iphone):
    item_iphone.apply_discount()
    assert item_iphone.price == 40000