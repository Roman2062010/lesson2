print("Сейчас мы определим, чем вам заниматься на основании введенного вами возраста!")

def age(x):
    if x <= 0:
        return "Ошибка! Введите целое число больше нуля!"
    if 1 <= x <= 7:
        return "Тебе пора в детский сад!"
    elif 8 <= x <= 16:
        return "Тебе пора в школу!"
    elif 17 <= x <= 22:
        return "Тебе пора в институт!"
    elif 23 <= x <= 64:
        return "Вам пора на работу!"
    elif x >= 65:
        return "Отдыхай, дружище, ты на пенсии!"
while True:   
    try:
        x = int(input("Введите ваш возраст: "))
        print(age(x))
       
    except ValueError:
        print("Ошибка! Введите целое число!")

    x = int(input("Введите ваш возраст: ")) 

    print(age(x))
