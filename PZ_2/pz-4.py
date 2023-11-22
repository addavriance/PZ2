import math

sin = 0
x = float(input("Введите x: "))

for n in range(13):
    term = ((-1) ** n) * (x ** (2 * n + 1)) / math.factorial(2 * n + 1)
    sin += term

print(f"Приближенное значение синуса: {sin}")
