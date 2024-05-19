"""
Вариант 19.
2. Составить генератор (yield), который преобразует все буквенные символы в заглавные.
"""

m_str = input("Введите строку: ")


def to_upper(phrase: str):
    for char in phrase:
        yield char.upper() if char.isalpha() else char


print("".join(to_upper(m_str)))
