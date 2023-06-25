# 1

first_number = int(input())
second_number = int(input())
third_number = int(input())
fourth_number = int(input())
final_result = (first_number + second_number) // third_number * fourth_number
print(final_result)

# 2

first_character = input()
second_character = input()
third_character = input()
total_string = first_character + second_character + third_character
print(total_string)

# 3

from math import ceil

number_of_people = int(input())
elevator_capacity = int(input())
number_of_courses = ceil(number_of_people / elevator_capacity)
print(number_of_courses)

# 4

number_of_characters = int(input())
total_sum = 0
for character in range(number_of_characters):
    current_character = input()
    total_sum += ord(current_character)
print(f"The sum equals: {total_sum}")

# 5

start_index = int(input())
final_index = int(input())
for character in range(start_index, final_index + 1):
    print(chr(character), end=" ")

# 6

number_of_symbols = int(input())
for first_symbol in range(number_of_symbols):
    for second_symbol in range(number_of_symbols):
        for third_symbol in range(number_of_symbols):
            print(f"{chr(97 + first_symbol)}{chr(97 + second_symbol)}{chr(97 + third_symbol)}")

# 7


number_of_lines = int(input())
tank_capacity = 255
water_counter = 0
for current_line in range(number_of_lines):
    liters_of_water = int(input())
    if tank_capacity - liters_of_water < 0:
        print("Insufficient capacity!")
        continue
    tank_capacity -= liters_of_water
    water_counter += liters_of_water
print(water_counter)

# 8

companions = int(input())
days = int(input())
coins = 0
for current_day in range(1, days + 1):
    if current_day % 10 == 0:
        companions -= 2
    if current_day % 15 == 0:
        companions += 5
    if current_day % 3 == 0:
        coins -= 3 * companions
    if current_day % 5 == 0:
        coins += 20 * companions
        if current_day % 3 == 0:
            coins -= 2 * companions
    coins += 50
    coins -= 2 * companions
coins_per_companion = int(coins // companions)
print(f"{companions} companions received {coins_per_companion} coins each.")

# 9

number_of_snowballs = int(input())
max_weight = 0
max_time = 0
max_quality = 0
max_value = 0
for current_snowball in range(number_of_snowballs):
    current_weight = int(input())
    current_time = int(input())
    current_quality = int(input())
    current_value = (current_weight / current_time) ** current_quality
    if current_value > max_value:
        max_weight = current_weight
        max_time = current_time
        max_quality = current_quality
        max_value = current_value
print(f"{max_weight} : {max_time} = {int(max_value)} ({max_quality})")

# 10


number_of_lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total_helmets_broken = number_of_lost_fights // 2
total_swords_broken = number_of_lost_fights // 3
total_shields_broken = number_of_lost_fights // 6  # number_of_lost_fights // (2+3)
total_armors_broken = total_shields_broken // 2
expenses = helmet_price * total_helmets_broken + \
           sword_price * total_swords_broken + \
           shield_price * total_shields_broken + \
           armor_price * total_armors_broken
print(f"Gladiator expenses: {expenses:.2f} aureus")