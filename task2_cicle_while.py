
conv = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую"}

while True:
    user_say = input('Скажи что-нибудь: ')
    if user_say == "Как дела?":
        print(conv["Как дела?"])
    elif user_say == "Что делаешь?":
        print(conv["Что делаешь?"])
        break
    else:
        print('Сам ты {}'.format(user_say))
     


   