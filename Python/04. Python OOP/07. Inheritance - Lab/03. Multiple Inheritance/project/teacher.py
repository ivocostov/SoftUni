from MainProblem.project import Person
from MainProblem.project import Employee


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."
    