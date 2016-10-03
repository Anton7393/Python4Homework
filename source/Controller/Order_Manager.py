from Models.Order import Order
from Controller.ReceiptManager import ReceiptManager
from Controller.Interpreter import Interpreter
from datetime import datetime
from View.Message import Message

class Order_Manager:
    __list_of_receipts = []
    __is_another_order = True
    __receipt_manager = ReceiptManager()
    __intro_message = "Please input your orders here!"
    __another_order_message = "Type yes if you want to create another order"
    __name_input_message = "Please input your name:"

    def start(self):
        Message.show_message(self.__intro_message)
        while self.__is_another_order:
            self.__costumer_initialization()
            self.__make_order()
            self.__cook_order()
            self.__turn_to_another_order()

    def __costumer_initialization(self):
        name = Message.read(self.__name_input_message)
        current_time = datetime.now()
        self.__order = Order(name, current_time)

    def __make_order(self):
        list_of_receipts = self.__receipt_manager.start()
        self.__order.set_receipts(list_of_receipts)

    def __cook_order(self):
        Message.show_order(self.__order)

    def __turn_to_another_order(self):
        command = Message.read(self.__another_order_message)
        self.__is_another_order = Interpreter.is_yes(command)

