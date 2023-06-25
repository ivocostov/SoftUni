available_budget = float(input())
flour_per_kg_price = float(input())

eggs_pack_price = flour_per_kg_price * 0.75
milk_per_lt_price = flour_per_kg_price * 1.25

colored_eggs_counter = 0
recipe_value = eggs_pack_price + flour_per_kg_price + milk_per_lt_price / 4
number_of_loaves = int(available_budget / recipe_value)
available_budget -= number_of_loaves * recipe_value

for current_loaf in range(1, int(number_of_loaves) + 1):

    colored_eggs_counter += 3
    if current_loaf % 3 == 0:
        colored_eggs_counter -= current_loaf - 2

print(f"You made {int(number_of_loaves)} loaves of Easter bread! Now you have {colored_eggs_counter} eggs "
      f"and {available_budget:.2f}BGN left.")
