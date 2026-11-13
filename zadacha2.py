# Задача 2 – клас Student, наследник на Person

class Person:
    def __init__(self, name, family, age, nationality):
        self.name = name
        self.family = family
        self.age = age
        self.nationality = nationality

    def print(self):
        print("Име:", self.name, self.family, "| Националност:", self.nationality)


class Student(Person):
    def __init__(self, name, family, age, nationality, university, yearofstudy):
        super().__init__(name, family, age, nationality)
        self.university = university
        self.yearofstudy = yearofstudy

    def print(self):  # предефиниран метод
        super().print()
        print("   Университет:", self.university, "| Курс:", self.yearofstudy)


p1 = Person("Иван", "Петров", 35, "българин")
p1.print()

s1 = Student("Георги", "Иванов", 19, "българин", "ТУ-София", 1)
s2 = Student("Anna", "Schmidt", 21, "германка", "TU Munich", 3)

s1.print()
s2.print()
