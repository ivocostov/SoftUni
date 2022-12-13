# ad astra

import re

data = input()
pattern = r'(\#|\|)([a-z A-Z]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1'
result = re.findall(pattern, data)
print_result = ''
calories = 0

for elements in result:
    print_result += f"Item: {elements[1]}, Best before: {elements[2]}, Nutrition: {elements[3]}\n"
    calories += int(elements[-1])

number_of_days = int(calories / 2000)
print(f"You have food to last you for: {number_of_days} days!")
print(print_result)


# world tour
def world_tour(destinations):
    while True:
        command = input().split(':')
        current_command = command[0]

        if current_command == 'Travel':
            print(f'Ready for world tour! Planned stops: {destinations}')
            break

        elif current_command == 'Add Stop':
            index, string = int(command[1]), command[2]

            if 0 <= index < len(destinations):
                destinations = destinations[:index] + string + destinations[index:]

        elif current_command == 'Remove Stop':
            start_index, end_index = int(command[1]), int(command[2])

            if 0 <= start_index <= end_index < len(destinations):
                destinations = destinations[:start_index] + destinations[end_index + 1:]

        elif current_command == 'Switch':
            old_string, new_string = command[1], command[2]
            destinations = destinations.replace(old_string, new_string)

        print(destinations)


data = input()
world_tour(data)


# heroes of code and logic
def create_heroes(heroes_dict, number):
    for _ in range(number):
        data = input().split(' ')
        hero_name, hit_points, mana_points = data[0], int(data[1]), int(data[2])
        heroes_dict[hero_name] = [hit_points, mana_points]


def playing_game(heroes_dict):
    while True:
        command = input().split(' - ')

        if command[0] == 'End':
            break

        current_command = command[0]

        if current_command == 'CastSpell':
            hero_name, mp_needed, spell_name = command[1], int(command[2]), command[3]
            available_mp = heroes_dict[hero_name][1]

            if available_mp >= mp_needed:
                heroes_dict[hero_name][1] -= mp_needed
                current_mp = heroes_dict[hero_name][1]
                print(f"{hero_name} has successfully cast {spell_name} and now has {current_mp} MP!")
            else:
                print(f"{hero_name} does not have enough MP to cast {spell_name}!")

        elif current_command == 'TakeDamage':
            hero_name, damage, attacker = command[1], int(command[2]), command[3]
            available_hp = heroes_dict[hero_name][0]

            if available_hp - damage > 0:
                heroes_dict[hero_name][0] -= damage
                current_hp = heroes_dict[hero_name][0]
                print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {current_hp} HP left!")
            else:
                del heroes_dict[hero_name]
                print(f"{hero_name} has been killed by {attacker}!")

        elif current_command == 'Recharge':
            hero_name, amount = command[1], int(command[2])
            available_mp = heroes_dict[hero_name][1]

            if available_mp + amount > 200:
                amount = 200 - available_mp
                heroes_dict[hero_name][1] += amount
            else:
                heroes_dict[hero_name][1] += amount

            print(f"{hero_name} recharged for {amount} MP!")

        elif current_command == 'Heal':
            hero_name, amount = command[1], int(command[2])
            available_mp = heroes_dict[hero_name][0]

            if available_mp + amount > 100:
                amount = 100 - available_mp
                heroes_dict[hero_name][0] += amount
            else:
                heroes_dict[hero_name][0] += amount

            print(f"{hero_name} healed for {amount} HP!")


def print_function(heroes_dict):
    print_result = ''

    for hero in heroes_dict:
        print_result += f'{hero}\n  HP: {heroes_dict[hero][0]}\n  MP: {heroes_dict[hero][1]}\n'

    return print_result


def heroes_of_code(number):
    # In heroes_dict we have key - hero name and as value we have
    # a list with two elements: HP - index 0, MP - index 1
    heroes_dict = {}

    # This function will create our heroes by adding different specifics for them
    # like HP and MP. HP stands for hit po2ints and MP for mana points
    create_heroes(heroes_dict, number_of_heroes)

    # This is the main function in which the game will develop
    # according to certain conditions
    playing_game(heroes_dict)

    # print_function - Print all members of your party who are still alive
    # and their HP and MP
    print(print_function(heroes_dict))


number_of_heroes = int(input())
heroes_of_code(number_of_heroes)

# mirror words
import re

data = input()
pattern = r'(#|@)([A-Za-z]{3,})(\1{2})([A-Za-z]{3,})\1'
result = re.findall(pattern, data)
mirror_words = []
the_count_of_words = 0

for pair in result:
    if pair[1] == pair[3][::-1]:
        mirror_words.append(f'{pair[1]} <=> {pair[3]}')

    the_count_of_words += 1

if the_count_of_words > 0:
    print(f'{the_count_of_words} word pairs found!')

    if not mirror_words:
        print('No mirror words!')
    else:
        print('The mirror words are:')
        print(', '.join(mirror_words))

else:
    print('No word pairs found!')
    print('No mirror words!')


# decorator example
def decorator_func(fnc):
    def inner(list_of_names):
        return {val[0]: [val[1], val[2]] for val in list_of_names}

    return inner


@decorator_func
def main_function(*args):
    return args


number_of_heroes = int(input())
data = [input().split(' ') for _ in range(number_of_heroes)]
print(main_function(data)