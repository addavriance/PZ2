"""
Вариант 19

Организовать словарь avto, содержащий 3 ключа (марки авто) и списки из трех моделей в качестве значений.
Обеспечить отображение вторых моделей по каждому авто, всех моделей словаря.

"""

avto = {
    "Toyota": ["Toyota Camry", "Toyota Corolla", "Toyota Prius"],
    "Kia": ["Kia Sedona", "Kia Sorento", "Kia Optima"],
    "Subaru": ["Subaru Outback", "Subaru Forester", "Subaru BRZ"]
}

for i, j in avto.items():
    print(j[1])
