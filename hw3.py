def my_func():
    a = float(input('A =  '))
    b = float(input('B =  '))
    c = float(input('C =  '))
# Проверка на случаи введения равных значений
    if a == b and a == c: #*
        print('Введеные числа равны')
        return None

    elif a == b and a < c: #*
        print(f'Задано два равных минимальных числа')
        return None

    elif a == c and a < b:  #*
        print(f'Задано два равных минимальных числа')
        return None

    elif c == b and c < a: #*
        print(f'Задано два равных минимальных числа')
        return None

    elif a == b and a > c: #*
        print(f'Задано два равных наибольших числа с суммой {a + b}')
        return (a + b)

    elif a == c and a > b: #*
        print(f'Задано два равных наибольших числа с суммой {a + c}')
        return (a + c)

    elif c == b and c > a: #*
        print(f'Задано два равных наибольших числа с суммой {c + b}')
        return (c + b)

    else:
# Извлекаем наибольшие числа, путём удаления минимального элемента из списка
        list_n = [a, b, c]
        min_val = min(list_n)
        index_el = list_n.index(min_val)
        list_n.pop(index_el)
        v1 = float(list_n[0])
        v2 = float(list_n[1])
        result = v2+ v1
        print (f'Сумма двух наибольших чисел {v1} и {v2} равна {result}')
        return result


my_func()
