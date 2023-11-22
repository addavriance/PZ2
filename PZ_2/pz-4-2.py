n = int(input("Введите целое число > 0: "))
summ = 0
for i in range(1, n+1):
    summ += i**(n+1-i)

print(summ)