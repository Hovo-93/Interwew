"""
1. Проверить механизм наследования в Python. Для этого создать два класса. Первый — родительский (ItemDiscount),
должен содержать статическую информацию о товаре: название и цену. Второй — дочерний (ItemDiscountReport),
должен содержать функцию (get_parent_data), отвечающую за отображение информации о товаре в одной строке.
Проверить работу программы, создав экземпляр (объект) родительского класса
"""


class ItemDiscount:
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'{self.product_name} стоит {self.price} руб.'


test1 = ItemDiscountReport('mac_book_14', 199000)
print(test1.get_parent_data())
