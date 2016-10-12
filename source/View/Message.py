from Models.ProductsRosster import products_rooster


class Message:
    __border = "======================================================================="
    __storage_message = "Available products and indexes:"
    __help_message = "Enter -go for complete your order"

    @staticmethod
    def show_message(message):
        Message.__print_border()
        print (message)

    @staticmethod
    def read(message):
        Message.show_message(message)
        return str(input())

    @staticmethod
    def show_order(order):
        Message.__show_name(order.get_costumers_name())
        Message.__show_time(order.get_time())
        Message.__show_receipts(order.get_all_receipts())

    @staticmethod
    def show_help(storage):
        Message.__print_border()
        Message.__show_storage(storage)
        print(Message.__help_message)

    @staticmethod
    def __show_name(name):
        print ("Ordered by: {0}".format(name))

    @staticmethod
    def __show_time(date_and_time):
        year = date_and_time.year
        month = date_and_time.month
        day = date_and_time.day
        hour = date_and_time.hour
        minute = date_and_time.minute
        second = date_and_time.second
        print ("Order time: {0}-{1}-{2} on {3}:{4}:{5}".format(year, month, day, hour, minute, second))

    @staticmethod
    def __show_receipts(receipt_list):
        for receipt in receipt_list:
            Message.__show_receipt(receipt)

    @staticmethod
    def __show_receipt(receipt):
        receipt_name = receipt.get_name()
        ingredients = receipt.get_all_products()
        print ("Receipt: {0}".format(receipt_name))
        Message.__show_ingredients(ingredients)
        Message.__print_border()

    @staticmethod
    def __show_ingredients(products):
        for product in products:
            name = product.get_name()
            value = product.get_value()
            print ("{0} - {1}".format(name, value))

    @staticmethod
    def __print_new_line():
        print("\n")

    @staticmethod
    def __print_border():
        print(Message.__border)

    @staticmethod
    def __show_storage(storage):
        print(Message.__storage_message)
        products = storage.get_products()
        for article in products:
            print("{} - {} : {}".format(article, products_rooster[article], products[article]))

    @staticmethod
    def show_rooster():
        output = str()
        for product in products_rooster:
            output += '{} - {}\n'.format(product, products_rooster[product])
        return output



