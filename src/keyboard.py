from src.item import Item


class MixinLang():
    languages = ['EN', 'RU']
    def __init__(self, *args, **kwargs):
        #print("Start Mixin")
        super().__init__(*args, **kwargs)
        self.__language = self.languages[0]

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.language == "EN":
            self.__language = self.languages[1]
        else:
            self.__language = self.languages[0]
        return self


class KeyBoard(MixinLang, Item):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)




