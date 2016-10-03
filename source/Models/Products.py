class Products:
    __name = 'n/a'
    __value = 0
    __article = 'n/a'

    def __init__(self, name, value, article):
        self.__name = name
        self.__value = value
        self.__article = article

    def set_value(self, value):
        self.__value = value

    def get_value(self):
        return self.__value

    def get_article(self):
        return self.__article

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
