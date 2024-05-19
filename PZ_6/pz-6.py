"""
Вариант 19.
Дан список размера N и целые числа К и L (1 < К < L < N).
Найти сумму элементов списка с номерами от К до L включительно.
"""

import random

N = 10
K = 2
L = 7

my_list = [random.randint(1, 100) for _ in range(N)]

result_sum = sum(my_list[K-1:L])

print("Исходный список:", my_list)
print(f"Сумма элементов от K({K}) до L({L}):", result_sum)
