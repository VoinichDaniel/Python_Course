number1 = int(input('enter first number '))
number2 = int(input('enter second number '))
number3 = int(input('enter third number '))
number1 > 0 and number2 > 0 and number3 > 0
print('Нет нулевых значений!!!')
number1 == 0 or number2 == 0 or number3 == 0
print('здесь нужно вывести нулевое значение')
number1 == 0 and number2 == 0 and number3 == 0
print('Введены все нули!')
if number1 > (number2 + number3):
    print(number1 - number2 - number3)
elif number1 < (number2 + number3):
    print(number2 + number3 - number1)
elif number1 > 50 and (number2 > number1 or number3 > number1):
    print('Вася')
elif number1 > 5 or (number2 == 7 and number3 == 7):
    print('Петя')
