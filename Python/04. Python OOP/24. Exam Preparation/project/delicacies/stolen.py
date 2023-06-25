from MainProblem.project import Delicacy


class Stolen(Delicacy):

    @property
    def stolen_portion(self):
        return 250

    def __init__(self, name: str, price: float):
        super().__init__(name, self.stolen_portion, price)

    def details(self):
        return f"Stolen {self.name}: {self.stolen_portion}g - {self.price:.2f}lv."
