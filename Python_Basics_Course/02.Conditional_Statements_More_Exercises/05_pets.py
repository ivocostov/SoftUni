from math import ceil, floor
days_away = int(input())
food_in_kg = int(input())
dog_food_per_day_in_kg = float(input())
cat_food_per_day_in_kg = float(input())
turtle_food_per_day_in_grams = float(input())

total_dog_food_needed = days_away * dog_food_per_day_in_kg
total_cat_food_needed = days_away * cat_food_per_day_in_kg
total_turtle_food_needed = days_away * turtle_food_per_day_in_grams
turtle_food_gr_to_kg = total_turtle_food_needed / 1000

total_food_needed_in_kg = total_dog_food_needed + total_cat_food_needed + turtle_food_gr_to_kg

food_difference = abs(food_in_kg - total_food_needed_in_kg)

if food_in_kg >= total_food_needed_in_kg:
    print(f"{floor(food_difference)} kilos of food left.")
else:
    print(f"{ceil(food_difference)} more kilos of food are needed.")
