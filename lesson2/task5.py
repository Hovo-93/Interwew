"""
5. Реализовать расчет цены товара со скидкой. Величина скидки должна передаваться в качестве аргумента в дочерний класс.
Выполнить перегрузку методов конструктора дочернего класса (метод init, в который должна передаваться
переменная — скидка), и перегрузку метода str дочернего класса. В этом методе должна пересчитываться цена
и возвращаться результат — цена товара со скидкой. Чтобы все работало корректно, не забудьте инициализировать
дочерний и родительский классы (вторая и третья строка после объявления дочернего класса).
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
    def __init__(self, product_name, price, discount):
        super().__init__(product_name, price)
        self.discount = discount

    # def get_parent_data(self):
    #     return f'{self.get_name()} стоит {self.get_price()} руб.'

    def __str__(self):
        return f'Цена товара со скидкой {self.get_price() - (self.get_price() * self.discount) / 100}руб'


b = ItemDiscountReport('meat', 500, 20)
print(b.__str__())
