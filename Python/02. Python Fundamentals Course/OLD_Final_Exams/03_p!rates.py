<<<<<<< HEAD
def plunder(town, people, gold):
    if town in city_dictionary.keys():
        city_dictionary[town][0] -= people
        city_dictionary[town][1] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if city_dictionary[town][0] <= 0 or city_dictionary[town][1] <= 0:
            del city_dictionary[town]
            print(f"{town} has been wiped off the map!")


def prosper(town, gold):
    if town in city_dictionary.keys():
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            city_dictionary[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {city_dictionary[town][1]} gold.")


city_dictionary = {}

while True:
    command = input()
    if command == 'Sail':
        break
    current_command = command.split('||')

    city, population, gold = current_command[0], int(current_command[1]), int(current_command[2])

    if city not in city_dictionary.keys():
        city_dictionary[city] = [population, gold]
    else:
        city_dictionary[city][0] += population
        city_dictionary[city][1] += gold

while True:
    new_command = input()
    if new_command == 'End':
        break

    current_new_command = new_command.split('=>')

    action = current_new_command[0]
    if action == 'Plunder':
        town = current_new_command[1]
        people = int(current_new_command[2])
        gold = int(current_new_command[3])
        plunder(town, people, gold)
    elif action == 'Prosper':
        town = current_new_command[1]
        gold = int(current_new_command[2])
        prosper(town, gold)


print(f"Ahoy, Captain! There are {len(city_dictionary)} wealthy settlements to go to:")
for city, values in city_dictionary.items():
    print(f"{city} -> Population: {values[0]} citizens, Gold: {values[1]} kg")
=======
def plunder(town, people, gold):
    if town in city_dictionary.keys():
        city_dictionary[town][0] -= people
        city_dictionary[town][1] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if city_dictionary[town][0] <= 0 or city_dictionary[town][1] <= 0:
            del city_dictionary[town]
            print(f"{town} has been wiped off the map!")


def prosper(town, gold):
    if town in city_dictionary.keys():
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            city_dictionary[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {city_dictionary[town][1]} gold.")


city_dictionary = {}

while True:
    command = input()
    if command == 'Sail':
        break
    current_command = command.split('||')

    city, population, gold = current_command[0], int(current_command[1]), int(current_command[2])

    if city not in city_dictionary.keys():
        city_dictionary[city] = [population, gold]
    else:
        city_dictionary[city][0] += population
        city_dictionary[city][1] += gold

while True:
    new_command = input()
    if new_command == 'End':
        break

    current_new_command = new_command.split('=>')

    action = current_new_command[0]
    if action == 'Plunder':
        town = current_new_command[1]
        people = int(current_new_command[2])
        gold = int(current_new_command[3])
        plunder(town, people, gold)
    elif action == 'Prosper':
        town = current_new_command[1]
        gold = int(current_new_command[2])
        prosper(town, gold)


print(f"Ahoy, Captain! There are {len(city_dictionary)} wealthy settlements to go to:")
for city, values in city_dictionary.items():
    print(f"{city} -> Population: {values[0]} citizens, Gold: {values[1]} kg")
>>>>>>> 36496de6931529b811d0c463d6ad38e232c5703a
