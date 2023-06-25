class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}"


class Student(Person):                                # клас Student наследява class Person
    def __init__(self, name, age, rollno):
        super().__init__(name, age)                   # взима name и age и ги подава на Person __init__
        self.rollno = rollno


    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Roll No: {self.rollno}"


person = Person("John", 30)
student = Student('Mike', 20, 123)

# ######################################################################################################################

def kick_player(self, player_name: str):
    try:
        player = next(filter(lambda p: p.name == player_name, self.players))  # p.name взема името на player_name. Това е необходимо,
                                                                              # защото player_name е стринг и няма инстанция
                                                                              # а по този начин можем да вземем инстанцията
    except StopIteration:                                                     # next(filter()) ще върне първото намерено съвпадение и ще брейкне
        return f"Player {player_name} is not in the guild."                   # ако извикаме next() без filter() ще върне първото нещо в списъка
                                                                              # при повторно извикване ще върне второто и т.н.
    self.players.remove(player)
    player.guild = Player.NOT_IN_GUILD
    return f"Player {player_name} has been removed from the guild."

# ######################################################################################################################


from MainProblem.project import Animal


class Tiger(Animal):
    MONEY_FOR_CARE = 45

    def __init__(self, name: str, gender: str, age: int):
        super().__init__(name, gender, age, Tiger.MONEY_FOR_CARE)


# ######################################################################################################################

from MainProblem.project import Dessert


class Cake(Dessert):
    GRAMS = 250
    CALORIES = 1000
    PRICE = 5

    def __init__(self, name):                                           # подава се само това което иска parent class
        super().__init__(name, Cake.PRICE, Cake.GRAMS, Cake.CALORIES)   # останалото се подава в super()

# ######################################################################################################################





# ######################################################################################################################





# ######################################################################################################################






# ######################################################################################################################






# ######################################################################################################################