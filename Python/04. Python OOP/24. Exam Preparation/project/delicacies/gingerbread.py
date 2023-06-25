from MainProblem.project import Delicacy


class Gingerbread(Delicacy):

    @property
    def gingerbread_portion(self):
        return 200

    def __init__(self, name: str, price: float):
        super().__init__(name, self.gingerbread_portion, price)


    def details(self):
        return f"Gingerbread {self.name}: {self.gingerbread_portion}g - {self.price:.2f}lv."



