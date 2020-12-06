correct_input = False
while not correct_input:

    price = input("Введите цену товара: ")
    discount = input("Введите скидку на товар: ")
    max_discount = input("Введите максимальную скидку на товар: ")

    try:
        price = float(price)
        discount = float(discount)
        max_discount = int(max_discount)
    except (ValueError, TypeError):
        print("Вы ввели некоректные данные")
    else:
        x = price - (price * discount / 100)
        print(x)
        correct_input = True
       




   

    