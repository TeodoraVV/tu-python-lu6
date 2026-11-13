# Задача 3 – клас Lecturer, наследник на Person (+ кода от Задачи 1 и 2)

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

    def print(self):
        super().print()
        print("   Университет:", self.university, "| Курс:", self.yearofstudy)


class Lecturer(Person):
    def __init__(self, name, family, age, nationality, university, experience):
        super().__init__(name, family, age, nationality)
        self.university = university
        self.experience = experience

    def print(self):  # предефиниран метод
        super().print()
        print("   Университет:", self.university, "| Стаж:", self.experience, "г.")


p1 = Person("Иван", "Петров", 35, "българин")
s1 = Student("Георги", "Иванов", 19, "българин", "ТУ-София", 1)
l1 = Lecturer("Мария", "Димитрова", 48, "българка", "ТУ-София", 20)
l2 = Lecturer("John", "Smith", 55, "британец", "Oxford", 30)

p1.print()
s1.print()
l1.print()
l2.print()
