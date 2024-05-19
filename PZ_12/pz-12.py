"""
Вариант 19.
1. В последовательности на n целых элементов найти среднее арифметическое элементов первой трети.
"""

import random

n = int(input("Введите n: "))

mas = [random.randint(-100, 100) for i in range(n)]

first_third_len = len(mas) // 3

average = sum(mas[:first_third_len])/first_third_len

print(f"Сгенерированная последовательность: {mas}")
print(f"Среднее арифметическое первой трети последовательности: {average}")
