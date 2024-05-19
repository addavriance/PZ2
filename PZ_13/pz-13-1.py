"""
Вариант 19.
2. Перенести в новую матрицу Matr1 элементы, которые не находятся в первых и последних строках и столбцах матрицы Matr2 произвольного размера.
"""

from random import randint

rows = randint(1, 5)
columns = randint(1, 5)

Matr2 = [[randint(-100, 100) for j in range(rows)] for i in range(columns)]


print(f"Исходная матрица Matr2:\n ")
for row in Matr2:
    print(row)


def extract_inner_elements(matrix):
    inner_elements = []
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    for i in range(1, num_rows - 1):
        row = []
        for j in range(1, num_cols - 1):
            row.append(matrix[i][j])
        inner_elements.append(row)

    return inner_elements


Matr1 = extract_inner_elements(Matr2)

print("\nНовая матрица Matr1:\n ")
for row in Matr1:
    print(row)