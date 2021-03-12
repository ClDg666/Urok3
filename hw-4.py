def my_func(x, y):
    """ 1 - способ """
    test = x ** y
    print('1-ый способ:' + str(test))

    """2 - способ - цикл while """
    y_abs = abs(y)
    i = y_abs
    s = 1
    while i > 0:
        s = s * x
        i = i - 1
    test_2 = 1 / s
    print('2-ый способ (с циклом while):' + str(test_2))

    """2 - способ - цикл for """
    s2 = 1
    i =  1
    for i in range(y_abs):
         s2 = s2 * x
         i += 1
    test_3 = 1/s2
    print('3-ый способ (с циклом for):' + str(test_3))

my_func(3,-7)
