# 1

name = input()
if name == "Johnny":
    print("Hello, my love!")
else:
    print(f"Hello, {name}!")

# 2

ages = int(input())
drink_type = ''
if ages <= 14:
    drink_type = "toddy"
elif ages <= 18:
    drink_type = "coke"
elif ages <= 21:
    drink_type = "beer"
else:  # elif ages > 21:
    drink_type = "whisky"
print(f"drink {drink_type}")

# 3

number_of_messages = int(input())
for message in range(number_of_messages):
    number = int(input())
    if number == 88:
        print("Hello")
    elif number == 86:
        print("How are you?")
    elif number < 88:
        print("GREAT!")
    else:  # elif number > 88
        print("Bye.")

# 4

divisor = int(input())
boundary = int(input())
for current_number in range(boundary, divisor, -1):
    if current_number % divisor == 0:
        break
print(current_number)

# 5

number_of_orders = int(input())
total_price = 0
for order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    amount_of_capsules_per_day = float(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif amount_of_capsules_per_day < 1 or amount_of_capsules_per_day > 2000:
        continue
    price = price_per_capsule * days * amount_of_capsules_per_day
    total_price += price
    print(f"The price for the coffee is: ${price:.2f}")
print(f"Total: ${total_price:.2f}")

# 6

number_of_strings = int(input())
for string in range(number_of_strings):
    current_string = input()
    if "," in current_string or \
            "." in current_string or \
            "_" in current_string:
        print(f"{current_string} is not pure!")
    else:
        print(f"{current_string} is pure.")

# 8

coffee_counter = 0
command = input()
while command != "END":
    if command.lower() == "coding" \
            or command.lower() == "dog" \
            or command.lower() == "cat" \
            or command.lower() == "movie":
        if command.islower():
            coffee_counter += 1
        else:  # command.isupper()
            coffee_counter += 2
    command = input()
if coffee_counter > 5:
    print("You need extra sleep")
else:
    print(coffee_counter)

# 10

first_string = input()
second_string = input()
last_printed_string = first_string
for character_index in range(len(first_string)):
    left_part = second_string[:character_index + 1]  # [0:character_index + 1 : 1]
    right_part = first_string[character_index + 1:]  # [character_index + 1 : len(first_string):1]
    current_string = left_part + right_part
    if current_string == last_printed_string:
        continue
    print(current_string)
    last_printed_string = current_string

# 11

budget = float(input())
one_kg_flour_price = float(input())
breads_counter = 0
colored_eggs_counter = 0
eggs_price = one_kg_flour_price * 0.75
milk_price = one_kg_flour_price * 1.25 / 4
one_bread_price = eggs_price + one_kg_flour_price + milk_price
while budget >= one_bread_price:
    budget -= one_bread_price
    breads_counter += 1
    colored_eggs_counter += 3
    if breads_counter % 3 == 0:
        colored_eggs_counter -= breads_counter - 2
print(
    f"You made {breads_counter} loaves of Easter bread! Now you have {colored_eggs_counter} eggs and {budget:.2f}BGN left.")

# 12

quantity = int(input())
remaining_days = int(input())
budget = 0
total_spirit = 0
ornament_set = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15
for current_day in range(1, remaining_days + 1):
    if current_day % 11 == 0:
        quantity += 2
    if current_day % 2 == 0:
        budget += ornament_set * quantity
        total_spirit += 5
    if current_day % 3 == 0:
        budget += (tree_skirt + tree_garland) * quantity
        total_spirit += 13
    if current_day % 5 == 0:
        budget += tree_lights * quantity
        total_spirit += 17
        if current_day % 3 == 0:
            total_spirit += 30
    if current_day % 10 == 0:
        total_spirit -= 20
        budget += tree_skirt + tree_garland + tree_lights
if remaining_days % 10 == 0:
    total_spirit -= 30
print(f"Total cost: {budget}")
print(f"Total spirit: {total_spirit}")