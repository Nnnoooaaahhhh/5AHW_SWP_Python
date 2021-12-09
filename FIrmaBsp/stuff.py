from enum import Enum


class Sex(Enum):
    Female = 0
    Male = 1


class Department(Enum):
    Verkauf = 0
    Einkauf = 1
    HR = 2


class Person():
    def __init__(self, sex, age, name, department):
        self.sex = sex
        self.age = age
        self.name = name
        self.department = department


class Mitarbeiter(Person):
    def __init__(self, sex, age, name, department, salary):
        super().__init__(sex, age, name, department)
        self.salary = salary


class Gruppenleiter(Mitarbeiter):
    def __init__(self, sex, age, name, department, salary, status):
        super().__init__(sex, age, name, department, salary)
        self.status = status


