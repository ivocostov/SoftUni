"""
The directory should be copied outside this directory

"""

from typing import List
from MainProblem.project import Pokemon


class Trainer:

    def __init__(self, name: str):
        self.name = name
        self.pokemons: List[Pokemon] = []               # листа ще пази лист от pokemon.Pokemon ( инстанции ), задава се както в __init__ какъв вид променлива ще е, в случая лист
                                                        # Pokemon е референция, защото е без скобите, ако е със скобите ще извикаме е функцията

    def add_pokemon(self, pokemon: Pokemon):  # тук pokemon е инстанция и може да се достъпват нейните параметри
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"  # това ще отиде във файла pokemon и ще върне това което е във функцията pokemon_details()
        return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str):  # тук pokemon_name е стринг !!!!!
        try:
            pokemon = next(filter(lambda p: p.name == pokemon_name, self.pokemons))  # next връща първото съвпадение и го връща, при повторно изпълнение връща второто и т.н
            #pokemon =  [p for p in self.pokemons if p.name == pokemon_name][0]       # ако вместо lambda има примерно ИТЕРИРУЕМ обект без условия
                                                                                     # ред 26 върши същата работа
        except StopIteration:
            return "Pokemon is not caught"

        self.pokemons.remove(pokemon)
        return f"You have released {pokemon_name}"

    # [Pokemon("Pikachu", 100), Pokemon("Charzard", 50)]
    # инстанцията се казва Pikachu и се запазва в p докато се итерира

    def trainer_data(self):
        pokemons_data = '\n'.join(f"- {p.pokemon_details()}" for p in self.pokemons)
        return f"Pokemon Trainer {self.name}\n" + \
               f"Pokemon count {len(self.pokemons)}\n" + \
               f"{pokemons_data}"


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
