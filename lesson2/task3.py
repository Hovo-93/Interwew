"""
3. Усовершенствовать родительский класс таким образом, чтобы получить доступ к защищенным переменным.
Результат выполнения заданий 1 и 2 должен быть идентичным.
"""


class ItemDiscount:
    def __init__(self, product_name, price):
        self.__product_name = product_name
        self.__price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'{self.__product_name} стоит {self.__price} руб.'


A = ItemDiscount('iPad', 999)
print(A._ItemDiscount__product_name)  # iPad
print(A._ItemDiscount__price)  # 999
