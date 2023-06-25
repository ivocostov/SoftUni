from abc import abstractmethod, ABC


class Person(ABC):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def have_birthday(self):
        self.age += 1

    @abstractmethod
    def work(self):
        ...


class Employee(Person):

    def work(self):
        print("working")


class Boss(Person):


    def work(self):
        print("taking risks")


instances = [Boss("Ivan", 20), Employee("Peter", 19)]

for instance in instances:
    pass