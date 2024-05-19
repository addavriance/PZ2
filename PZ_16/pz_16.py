"""
Вариант 19

1. Создайте класс «Студент», который имеет атрибуты имя, фамилия и оценки.
Добавьте методы для вычисления среднего балла и определения, является ли студент
отличником.
"""


class Student:
    def __init__(self, first_name, last_name, grades):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

    def is_excellent(self):
        return self.average_grade() >= 4.5


if __name__ == "__main__":
    student = Student("Иван", "Нетяженко", [5, 4, 4, 5, 5, 4, 5, 5, 5, 5])
    print(f"Среднее арифметическое: {student.average_grade()}")
    print(f"Студент {student.first_name} {student.last_name} отличник? {student.is_excellent()}")

    student2 = Student("Артем", "Старчиков", [5, 4, 4, 5, 5, 5, 5, 5, 4])
    print(f"Среднее арифметическое: {student2.average_grade()}")
    print(f"Студент {student2.first_name} {student2.last_name} отличник? {student2.is_excellent()}")