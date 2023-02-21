number = int(input('Введите количество журавликов (кратное 3):' ))
if number % 6 == 0:
    petiy = number/3/2
    katiy = number - number/3
    sergey = number/3/2
    print(f'Петя сделал {int(petiy)}, Катя сделала {int(katiy)}, Сергей сделал {int(sergey)}')
else: print('Не верное число')