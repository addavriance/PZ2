"""
Вариант 19
2. Даны две переменные целого типа: А и В.
Если их значения не равны, то присвоить каждой переменной сумму этих значений, а если равны, то присвоить переменным нулевые значения.
Вывести новые значения переменных А и В.
"""

# a = int(input("Введите целое число 1: "))
# b = int(input("Введите целое число 2: "))
#
# if a != b:
#     a = sum([a, b])
#     b = a
# else:
#     a = 0
#     b = 0
#
# print(a, b)

n = int(input("N: "))
num = 1
char = -1
variable = 0
num_sum = 0

for i in range(n):
    num += .1
    char = -char
    variable = round(num * char, 10)
    num_sum += variable

print(round(num_sum, 5))
