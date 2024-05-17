"""
Вариант 19.

Дано трехзначное число.
В нем зачеркнули первую справа цифру и приписали ее слева.
Вывести полученное число.
"""

num = None

while not (len(str(num)) == 3 and str(num).isnumeric()):
    num = input("Введите целое трехзначное число: ")
    if num.isnumeric() and len(str(num)) != 3:  # Если введеная строка состоит полностью из чисел, но длинна не 3
        print("Вы ввели не трехзначное число.")
    elif num.count(".") == 1 and num.replace(".", "").isnumeric():  # Если в введеной строке есть всего одна точка и строка без нее состоит полностью из цифр
        print("Вы ввели не целое число.")
    elif num[0] == "-" and num.count("-") == 1 and num.replace("-", "").isnumeric():
        print("Вы ввели отрицательное число.")
    elif not num.isnumeric():  # Если введеная строка не состоит из цифр
        print("Вы ввели не число.")
    else:
        num = int(num)

right_num = num % 10  # Получает первую цифру справа
first_second_num = num//10  # Получат первую и вторую цифру слева

result = right_num*100+first_second_num

print(f"Результат: {result}")
