
def strings (str_1, str_2):
    if type(str_1) != str or type(str_2) != str:
        return 0
    if str_1 == str_2:
        return 1
    if str_1 > str_2:
        return 2
    if str_1 < str_2:
        return 3


str_1 = str(input("Введите информацию в строку №1: "))
str_2 = str(input("Введите информацию в строку №2: "))

print(strings(str_1, str_2))