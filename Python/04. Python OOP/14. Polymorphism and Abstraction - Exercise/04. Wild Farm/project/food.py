from abc import ABC, abstractmethod


class Food(ABC):
    @abstractmethod                      # __init__ се прави абстрактен, защото няма друг абстрактен метод, а трябва да има поне един
    def __init__(self, quantity: int):
        self.quantity = quantity


class Vegetable(Food):
    def __init__(self, quantity: int):
        super().__init__(quantity)


class Fruit(Food):
    def __init__(self, quantity: int):
        super().__init__(quantity)


class Meat(Food):
    def __init__(self, quantity: int):
        super().__init__(quantity)


class Seed(Food):
    def __init__(self, quantity: int):
        super().__init__(quantity)

