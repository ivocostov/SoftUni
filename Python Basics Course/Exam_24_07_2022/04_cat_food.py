number_of_cats = int(input())
price_cat_food_per_kg = 12.45

small_cats_group = 0
big_cats_group = 0
huge_cats_group = 0
total_food_in_grams = 0

for cat in range(number_of_cats):
    current_food_in_grams = float(input())
    total_food_in_grams += current_food_in_grams

    if 100 <= current_food_in_grams < 200:
        small_cats_group += 1
    elif 200 <= current_food_in_grams < 300:
        big_cats_group += 1
    elif 300 <= current_food_in_grams < 400:
        huge_cats_group += 1

    daily_food_price = total_food_in_grams / 1000 * price_cat_food_per_kg

print(f"Group 1: {small_cats_group:} cats.")
print(f"Group 2: {big_cats_group:} cats.")
print(f"Group 3: {huge_cats_group:} cats.")
print(f"Price for food per day: {daily_food_price:.2f} lv.")
