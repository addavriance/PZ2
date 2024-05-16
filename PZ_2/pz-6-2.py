"""
Вариант 19.
Дан список размера N, все элементы которого, кроме последнего, упорядочены по возрастанию.
Сделать список упорядоченным, переместив последний элемент на новую позицию.
"""

import random

N = 8
max_int = 50

my_list = sorted([random.randint(1, max_int) for _ in range(N-1)]) + [random.randint(1, max_int)]

print("Исходный список:", my_list)

last_elem = my_list.pop()

_indexes = [i+1 for i in range(len(my_list)-1, -1, -1) if my_list[i] <= last_elem] + [0]
right_index = _indexes[0]

my_list.insert(right_index, last_elem)

print(f"\nПоследний элемент переставлен на {right_index} место.")
print("Исправленный список:", my_list)
