import pytest
from src.keyboard import KeyBoard
from src.item import Item


def test_keyboard():
    kb = KeyBoard("Logitech", 5000, 40)
    assert kb.name == "Logitech"
    assert kb.language == "EN"
    kb.change_lang().change_lang().change_lang()
    assert kb.language == 'RU'
    with pytest.raises(AttributeError, match="property 'language' of 'KeyBoard' object has no setter"):
        kb.language = 'FR'