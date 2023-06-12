import pytest
from src.phone import Phone
from src.item import Item

@pytest.fixture()
def phone_iphone():
    return Phone("Iphone 14", 50000, 20, 1)


#Testcase#1 Phone.__number_of_sim.getter
def test_number_of_sim__getter(phone_iphone):
    assert phone_iphone.number_of_sim == 1


#Testcase#2 Phone.__number_of_sim.setter
def test_number_of_sim_setter(phone_iphone):
    phone_iphone.number_of_sim = 2
    assert phone_iphone.number_of_sim == 2
    with pytest.raises(ValueError, match= "Количество физических SIM-карт должно быть целым числом больше нуля."):
        phone_iphone.number_of_sim = -1


#Testcase#3 Phone.__repr__
def test_repr(phone_iphone):
    assert repr(phone_iphone) == "Phone('Iphone 14', 50000, 20, 1)"

def test_add():
    item1 = Item("Смартфон", 10000, 20)
    phone1 = Phone("Samsung", 45000, 15, 1)
    assert item1 + phone1 == 35
    assert phone1 + phone1 == 30
    assert phone1 + 40 == None