from Models.ProductsRosster import products_rooster


class Storage:
    __storage_products = {}

    def __init__(self, count):
        self.__fill_storage_constant(count)

    def implements_receipt(self, receipt):
        self.__set_receipt(receipt)
        self.__substruction_receipt()
        self.__validate_storage()

    def get_products(self):
        return self.__storage_products

    def __fill_storage_constant(self, count):
        for article in products_rooster.items():
            self.__storage_products[article[0]] = count

    def __set_receipt(self, receipt):
        self.__receipt = receipt

    def __substruction_receipt(self):
        for ingredient in self.__receipt.get_all_products():
            self.__storage_products[ingredient.get_article()] -= ingredient.get_value()

    def __validate_storage(self):
        for ingredient in self.__storage_products:
            if self.__storage_products[ingredient] < 0:
                self.__storage_backup()
                self.__error()

    def __storage_backup(self):
        for ingredient in self.__receipt.get_ingredient():
            self.__storage_products[ingredient.get_article()] += ingredient.get_value()

    def __error(self):
        raise Exception('Not enough product in storage')

