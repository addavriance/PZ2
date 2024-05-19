"""
Вариант 19

3. Для задачи из блока 1 создать две функции, save_def и load _def, которые позволяют
сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно.
Использовать модуль pickle для сериализации и десериализации объектов Python в
бинарном формате.
"""

from pz_16 import Student
import pickle

assets_path = "../assets"


def save_students(data, filename):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)


def load_students(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)


student1 = Student("Иван", "Нетяженко", [5, 4, 4, 5, 5, 4, 5, 5, 5, 5])
student2 = Student("Артем", "Старчиков", [5, 4, 4, 5, 5, 5, 5, 5, 4])
student3 = Student("Екатерина", "Петрова", [4, 4, 5, 5, 5, 4, 5, 5, 5])

students = [student1, student2, student3]

save_students(students, f'{assets_path}/students.pickle')

loaded_students = load_students(f'{assets_path}/students.pickle')

for student in loaded_students:
    print(f"Среднее арифметическое: {student.average_grade()}")
    print(f"Студент {student.first_name} {student.last_name} отличник? {student.is_excellent()}")