"""
Вариант 19.
Дана строка, состоящая из русских слов, набранных заглавными буквами и разделенных пробелами (одним или несколькими).
Преобразовать каждое слово в строке, заменив в нем все предыдущие вхождения его последней буквы на символ «.» (точка).
Например, слово «МИНИМУМ» надо преобразовать в «.ИНИ.УМ». Количество пробелов между словами не изменять.
"""


def count_spaces_after_words(input_string):
    space_counts = []
    current_space_count = 0

    for i in range(len(input_string)):
        char = input_string[i]
        if char == ' ':
            current_space_count += 1
        else:
            space_counts.append(current_space_count) if current_space_count != 0 else ...
            current_space_count = 0

    if len(space_counts) < len(input_string.split()):
        space_counts.insert(0, 0)

    return space_counts


def process_text(text):
    words = text.split()
    spaces = count_spaces_after_words(text)

    result = []
    for i, word in enumerate(words):
        last_letter = word[-1]
        new_word = " " * spaces[i] + word[:-1].replace(last_letter, '.') + last_letter
        result.append(new_word)
    return ''.join(result)


input_text = input("Введите текст: ")

print(process_text(input_text))

