"""
Вариант 19.

Составить функцию решения задачи: из заданного числа вычли сумму его цифр.
Из результата вновь вычли сумму его цифр и т. д. Через сколько таких действий получится нуль?
"""


def find_steps_to_zero(num):
    steps = 0
    while num > 0:
        digit_sum = sum([int(digit) for digit in str(num)])
        num -= digit_sum
        steps += 1
    return steps


numb = int(input("Введите число: "))

print(find_steps_to_zero(numb))