"""
Вариант 19.
2. Из предложенного текстового файла (text18-19.txt) вывести на экран его содержимое, количество символов, принадлежащих к группе букв.
Сформировать новый файл, в который поместить текст в стихотворной форме предварительно заменив символы верхнего регистра на нижний.
"""

with open("../assets/text18-19.txt", "r+") as f:
    data = f.read()
    alpha_count = len([char for char in data if char.isalpha()])

    print(f"Содержимое:\n\n'{data}'\n\nКоличество букв: {alpha_count}")

    with open("../assets/processed-1.txt", "w+") as fl:
        fl.write(data.lower())