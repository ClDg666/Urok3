def divide2 (arg_1, arg_2):
    arg_1 = float(input('Введите делимое: '))
    arg_2 = float(input('Введите делитель: '))
    try:
        result = arg_1 / arg_2
    except ZeroDivisionError:
        print('Ошибка. Деление на ноль')
        result = None
    return result

print(divide2(2,3))
