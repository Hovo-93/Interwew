"""
2. Написать программу, которая запрашивает у пользователя ввод числа. На введенное число она отвечает сообщением,
целое оно или дробное. Если дробное — необходимо далее выполнить сравнение чисел до и после запятой.
Если они совпадают, программа должна возвращать значение True, иначе False.
"""
number = input('Введите число ')
# print("{:.2f}".format(number))
if number.isdecimal():
    print('Число целое')
elif str(number).split("."):
    print('Число дробное')
    mas = []
    for i in str(number).split('.'):
        mas.append(i)
    if mas[0] == mas[1]:
        print('True')
    else:
        print('False')

# res_int = isinstance(number, (int))
# if res_float == True:
#     print('Число дробное')
# elif res_int == True:
#     print('Число целое')
