"""
Вариант 19

2. Создание базового класса "Животное" и его наследование для создания классов
"Собака" и "Кошка". В классе "Животное" будут общие методы, такие как "дышать"
и "питаться", а классы-наследники будут иметь свои уникальные методы и свойства,
такие как "гавкать" и "мурлыкать".
"""


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def breathe(self):
        print(f"{self.name} дышит.")

    def eat(self):
        print(f"{self.name} кушает.")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} гавкает.")


class Cat(Animal):
    def purr(self):
        print(f"{self.name} мурлыкает.")


dog = Dog("Шарик", 3)
cat = Cat("Мурзик", 5)

dog.breathe()
dog.eat()
dog.bark()

cat.breathe()
cat.eat()
cat.purr()
