class Order:
    __list_of_receipts = []
    __name_of_costumer = 'n/a'

    def __init__(self, name, current_time):
        self.__name_of_costumer = name
        self.__datetime = current_time

    def get_time(self):
        return self.__datetime

    def get_costumers_name(self):
        return self.__name_of_costumer

    def get_all_receipts(self):
        return self.__list_of_receipts

    def add_receipt(self, receipt):
        self.__list_of_receipts.append(receipt)

    def set_receipts(self, receipts_list):
        self.__list_of_receipts = receipts_list
