from MainProblem.project import Dessert


class Cake(Dessert):
    GRAMS = 250
    CALORIES = 1000
    PRICE = 5

    def __init__(self, name):                                           # подава се само това което иска parent class
        super().__init__(name, Cake.PRICE, Cake.GRAMS, Cake.CALORIES)   # останалото се подава в super()

