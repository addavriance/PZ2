"""
Вариант 19.
1. В матрице найти среднее арифметическое элементов последних двух столбцов.
"""
from random import randint

rows = randint(1, 5)
columns = randint(1, 5)

matrix = [[randint(-1, 2) for j in range(rows)] for i in range(columns)]


def average_of_last_two_columns(matrix):
    num_rows = len(matrix)
    if num_rows == 0:
        return None

    num_cols = len(matrix[0])
    if num_cols < 2:
        return None

    total_sum = 0
    count = 0
    for row in matrix:
        total_sum += row[num_cols - 2] + row[num_cols - 1]
        count += 2

    return total_sum / count


avg = average_of_last_two_columns(matrix)

print("Исходная матрица:\n")
for row in matrix:
    print(row)

if avg is not None:
    print("\nСреднее арифметическое последних двух столбцов матрицы:", avg)
else:
    print("\nМатрица слишком мала для вычисления среднего арифметического последних двух столбцов.")