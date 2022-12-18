<<<<<<< HEAD
"""You need to categorize dragons by their type. For each dragon, identified by name, keep information about his stats
(damage, health, and armor). Type is preserved as in the order of input, but dragons are sorted alphabetically by
their name. For each type, you should also print the average damage, health, and armor of the dragons. For each dragon,
print his own stats.
There may be missing stats in the input, though. If a stat is missing you should assign it default values.
Default values are as follows: health 250, damage 45, and armor 10. Missing stat will be marked by "null".
The input is in the following format "{type} {name} {damage} {health} {armor}".
The "type" and the "name" are strings. The "damage", the "health", and the "armor" are integers. Any of the integers
may be assigned "null" value. See the examples below for better understanding of your task.
If the same dragon is added a second time, the new stats should overwrite the previous ones. Two dragons are considered
equal if they match by both name and type.
"""


def initial_dictionary(dragon_type, dragon_name, dragon_damage, dragon_health, dragon_armor):
    dragons_dictionary[dragon_type] = dragons_dictionary.get(dragon_type, {})
    dragons_dictionary[dragon_type][dragon_name] = dragons_dictionary.get(dragon_name, dict())
    dragons_dictionary[dragon_type][dragon_name][dragon_dmg] = dragon_damage
    dragons_dictionary[dragon_type][dragon_name][dragon_hp] = dragon_health
    dragons_dictionary[dragon_type][dragon_name][dragon_cp] = dragon_armor



def results():
    for color in dragons_dictionary.keys():
        damage_counter, health_counter, armor_counter = 0, 0, 0
        for name in dragons_dictionary[color].keys():
            damage_counter += dragons_dictionary[color][name][dragon_dmg]
            health_counter += dragons_dictionary[color][name][dragon_hp]
            armor_counter += dragons_dictionary[color][name][dragon_cp]
        all_dragons = len(dragons_dictionary[color])
        print(f"{color}::({damage_counter / all_dragons:.2f}/{health_counter / all_dragons:.2f}/{armor_counter / all_dragons:.2f})")
        for current_name in sorted(dragons_dictionary[color].keys()):
            print(f"-{current_name} -> damage: {dragons_dictionary[color][current_name][dragon_dmg]}, "
                  f"health: {dragons_dictionary[color][current_name][dragon_hp]}, "
                  f"armor: {dragons_dictionary[color][current_name][dragon_cp]}")


number_of_dragons = int(input())
dragons_dictionary = {}
dragon_dmg, dragon_hp, dragon_cp = 'damage', 'health', 'armor'

for _ in range(number_of_dragons):
    dragon_type, dragon_name, damage, health, armor = input().split()

    if damage == 'null':
        dragon_damage = 45
    else:
        dragon_damage = int(damage)
    if health == 'null':
        dragon_health = 250
    else:
        dragon_health = int(health)
    if armor == 'null':
        dragon_armor = 10
    else:
        dragon_armor = int(armor)

    initial_dictionary(dragon_type, dragon_name, dragon_damage, dragon_health, dragon_armor)

results()
=======
"""You need to categorize dragons by their type. For each dragon, identified by name, keep information about his stats
(damage, health, and armor). Type is preserved as in the order of input, but dragons are sorted alphabetically by
their name. For each type, you should also print the average damage, health, and armor of the dragons. For each dragon,
print his own stats.
There may be missing stats in the input, though. If a stat is missing you should assign it default values.
Default values are as follows: health 250, damage 45, and armor 10. Missing stat will be marked by "null".
The input is in the following format "{type} {name} {damage} {health} {armor}".
The "type" and the "name" are strings. The "damage", the "health", and the "armor" are integers. Any of the integers
may be assigned "null" value. See the examples below for better understanding of your task.
If the same dragon is added a second time, the new stats should overwrite the previous ones. Two dragons are considered
equal if they match by both name and type.
"""


def initial_dictionary(dragon_type, dragon_name, dragon_damage, dragon_health, dragon_armor):
    dragons_dictionary[dragon_type] = dragons_dictionary.get(dragon_type, {})
    dragons_dictionary[dragon_type][dragon_name] = dragons_dictionary.get(dragon_name, dict())
    dragons_dictionary[dragon_type][dragon_name][dragon_dmg] = dragon_damage
    dragons_dictionary[dragon_type][dragon_name][dragon_hp] = dragon_health
    dragons_dictionary[dragon_type][dragon_name][dragon_cp] = dragon_armor



def results():
    for color in dragons_dictionary.keys():
        damage_counter, health_counter, armor_counter = 0, 0, 0
        for name in dragons_dictionary[color].keys():
            damage_counter += dragons_dictionary[color][name][dragon_dmg]
            health_counter += dragons_dictionary[color][name][dragon_hp]
            armor_counter += dragons_dictionary[color][name][dragon_cp]
        all_dragons = len(dragons_dictionary[color])
        print(f"{color}::({damage_counter / all_dragons:.2f}/{health_counter / all_dragons:.2f}/{armor_counter / all_dragons:.2f})")
        for current_name in sorted(dragons_dictionary[color].keys()):
            print(f"-{current_name} -> damage: {dragons_dictionary[color][current_name][dragon_dmg]}, "
                  f"health: {dragons_dictionary[color][current_name][dragon_hp]}, "
                  f"armor: {dragons_dictionary[color][current_name][dragon_cp]}")


number_of_dragons = int(input())
dragons_dictionary = {}
dragon_dmg, dragon_hp, dragon_cp = 'damage', 'health', 'armor'

for _ in range(number_of_dragons):
    dragon_type, dragon_name, damage, health, armor = input().split()

    if damage == 'null':
        dragon_damage = 45
    else:
        dragon_damage = int(damage)
    if health == 'null':
        dragon_health = 250
    else:
        dragon_health = int(health)
    if armor == 'null':
        dragon_armor = 10
    else:
        dragon_armor = int(armor)

    initial_dictionary(dragon_type, dragon_name, dragon_damage, dragon_health, dragon_armor)

results()
>>>>>>> 36496de6931529b811d0c463d6ad38e232c5703a
