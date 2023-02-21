number = int(input('Введите шестизначное число:' ))
if 99999 < number < 1000000:
    numberFirst = number // 1000
    numberSecond = number % 1000
    sumFirst = numberFirst // 100 + numberFirst % 10 + numberFirst // 10 % 10
    sumSecond = numberSecond // 100 + numberSecond % 10 + numberSecond // 10 % 10
    if sumFirst == sumSecond:
        print(number, '-> счастливое число')
    else: print(number, '-> не счастливое число')
else: print('Введино не верное число')
