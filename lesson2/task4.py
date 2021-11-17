"""
4. Реализовать возможность переустановки значения цены товара. Необходимо, чтобы и родительский, и дочерний классы
получили новое значение цены. Следует проверить это, вызвав соответствующий метод родительского класса и функцию
дочернего (функция, отвечающая за отображение информации о товаре в одной строке).
"""


class ItemDiscount:
    def __init__(self, product_name, price):
        self.__product_name = product_name
        self.__price = price

    def get_name(self):
        return self.__product_name

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'{self.get_name()} стоит {self.get_price()} руб.'


A = ItemDiscount('meat', 500)
B = ItemDiscountReport('meat', 500)
A.set_price(1500)
B.set_price(1500)
print(A.get_price(), A.get_name())
print(B.get_parent_data())
