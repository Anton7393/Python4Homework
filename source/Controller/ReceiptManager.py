from Models.Receipt import Receipt
from Models.Storage import Storage
from Models.Products import Products
from Models.ProductsRosster import products_rooster
from View.Message import Message
from Controller.Interpreter import Interpreter


class ReceiptManager:
    __storage = Storage(20)
    __intro_message = "Create your receipt!\n" \
                      "Type ? to watch help and current storage state\n" \
                      "Type -go to abort receipt and continue"
    __storage_error = "Storage error"
    __invalid_statement = "Please input correct statement!"
    __name_message = "Input name of your receipt:"
    __ingredients_message = Message.show_rooster() + "Input ingredients articles from list you want thought space"

    def __init__(self):
        self.__is_next_receipt = True
        self.__list_of_receipts = []

    def start(self):
        try:
            while self.__get_receipt():
                pass
        except Exception as ex:
            pass
        return self.__list_of_receipts

    def __get_receipt(self):
        Message.show_message(self.__intro_message)
        self.__get_receipt_name()
        self.__get_receipt_ingredients()
        self.__make_receipt()
        self.__validate_receipt()
        self.__list_of_receipts.append(self.__receipt)
        return True

    def __get_receipt_name(self):
        self.__name = self.__get_input(self.__name_message, lambda string: False)

    def __get_receipt_ingredients(self):
        sequence = self.__get_input(self.__ingredients_message, Interpreter.is_articles_correct)
        self.__article_list = sequence.split(' ')
        try:
            self.__article_list.remove('')
        except Exception:
            pass

    def __get_input(self, message, predicate):
        sting = Message.read(message)
        Interpreter.is_go(sting)
        while Interpreter.is_help(sting):
            Message.show_help(self.__storage)
            sting = Message.read(message)
            Interpreter.is_go(sting)
        while predicate(sting):
            Message.show_message(self.__invalid_statement)
            sting = Message.read(message)
            Interpreter.is_go(sting)
        return sting

    def __make_receipt(self):
        list_of_products = self.__make_list_of_products()
        self.__receipt = Receipt(self.__name, list_of_products)

    def __make_list_of_products(self):
        list_of_products = []
        product_dictionary = {}
        for product in products_rooster:
            product_dictionary[product] = 0
        for article in self.__article_list:
            product_dictionary[article] += 1
        for product in product_dictionary:
            if product_dictionary[product] > 0:
                list_of_products.append(Products(products_rooster[product], product_dictionary[product], product))
        return list_of_products

    def __validate_receipt(self):
        try:
            self.__storage.implements_receipt(self.__receipt)
        except Exception:
            Message.show_message(self.__storage_error)



