# Задача 1 – клас Person

class Person:
    def __init__(self, name, family, age, nationality):
        self.name = name
        self.family = family
        self.age = age
        self.nationality = nationality

    def print(self):
        print("Име:", self.name, self.family, "| Националност:", self.nationality)


p1 = Person("Иван", "Петров", 35, "българин")
p2 = Person("Maria", "Rossi", 28, "италианка")

p1.print()
p2.print()
