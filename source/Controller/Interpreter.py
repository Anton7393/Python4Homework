from Models.ProductsRosster import products_rooster


class Interpreter:
    __yes = "yes"
    __help = "?"
    __go = "-go"

    @staticmethod
    def is_yes(string):
        if Interpreter.__yes == string:
            return True
        else:
            return False

    @staticmethod
    def is_help(string):
        if Interpreter.__help == string:
            return True
        else:
            return False

    @staticmethod
    def is_go(string):
        if Interpreter.__go == string:
            raise Exception()

    @staticmethod
    def is_articles_correct(articles_sequence):
        articles_list = articles_sequence.split(' ')
        try:
            articles_list.remove('')
        except(Exception):
            pass
        if not articles_list:
            return True
        for article in articles_list:
            if article not in products_rooster.keys():
                return True
        return False

