class Matrix:
    def __init__(self, input_data, id):
        self.input = input_data
        self.id = id

    def __str__(self):
        print('матрица - id: ' + str(self.id))
        return '\n'.join([' '.join(map(str, line)) for line in self.input])

    def __add__(self, other):
        summa = ''
        l1 = len(self.input)
        l2 = len(other.input)
        if l1 == l2:
            for line_1, line_2 in zip(self.input, other.input):
                summed_line = [x + y for x, y in zip(line_1, line_2)]
                summa += ' '.join(map(str, summed_line)) + '\n'
        else:
            return 'Размеры матриц не совпадают'
        return summa


matrix1 = Matrix([[10, 23, 12],[33, 42, 47], [50, 62, 74], [37, 86,65]], 1)
matrix2 = Matrix([[27, 34, 45], [94, 75, 78], [36, 87, 32], [10, 20, 74]], 2)

print(matrix1)
print(matrix2)

print('Сумма матриц: ' + str(matrix1.id) + ' и ' + str(matrix2.id))
print(matrix1 + matrix2)  # matrix_1.__add__(matrix_2)