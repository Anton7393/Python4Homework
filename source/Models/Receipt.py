class Receipt:
    __original_name = 'n/a'
    __list_of_products = []

    def __init__(self, original_name, list_of_products):
        self.__original_name = original_name
        self.__list_of_products = list_of_products

    def add_products(self, product):
        self.__list_of_products.append(product)

    def get_name(self):
        return self.__original_name

    def get_all_products(self):
        return self.__list_of_products
