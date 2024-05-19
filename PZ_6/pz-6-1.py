"""
Вариант 19.
Дан целочисленный список размера N. Найти количество различных элементов в данном списке.
"""

import random

N = 15

my_list = [random.randint(1, 10) for _ in range(N)]

unique_count = len(set(my_list))

print("Исходный список:", my_list)
print("Количество различных элементов:", unique_count)
