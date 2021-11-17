"""
2. Инкапсулировать оба параметра (название и цену) товара родительского класса.
Убедиться, что при сохранении текущей логики работы программы будет сгенерирована ошибка выполнения.
"""


class ItemDiscount:
    def __init__(self, product_name, price):
        self.__product_name = product_name
        self.__price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'{self.__product_name} стоит {self.__price} руб.'


test = ItemDiscount('iphone', 65000)
print(test.product_name) #AttributeError: 'ItemDiscount' object has no attribute '_product_name'

