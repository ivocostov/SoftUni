from MainProblem.project import Cat


class Kitten(Cat):
    def __init__(self, name, age, gender="Female"):
        super().__init__(name, age, gender)
        #self.gender = gender

    def make_sound(self):
        return "Meow"