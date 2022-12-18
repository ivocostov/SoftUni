<<<<<<< HEAD
# 1


current_input = input().split()
symbols = ''.join(current_input)
letters = {}
for symbol in symbols:
    if symbol not in letters.keys():
        letters[symbol] = 0
    letters[symbol] += 1
for char, occurrences in letters.items():
    print(f"{char} -> {occurrences}")

# 2


resources = {}
while True:
    current_resource = input()
    if current_resource == "stop":
        break
    current_quantity = int(input())
    if current_resource not in resources.keys():
        resources[current_resource] = 0
    resources[current_resource] += current_quantity
for resource, quantity in resources.items():
    print(f"{resource} -> {quantity}")

# 3

countries = input().split(", ")
capitals = input().split(", ")
final_result = {countries[index]: capitals[index] for index in range(len(countries))}
# final_result = dict(zip(countries, capitals))
for country, capital in final_result.items():
    print(f"{country} -> {capital}")

# 4

phonebook = {}
while True:
    entry = input()
    if "-" not in entry:
        break
    name, phone = entry.split("-")
    phonebook[name] = phone
for check in range(int(entry)):
    searched_name = input()
    if searched_name in phonebook.keys():
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")

# 5

items = {"shards": 0, "fragments": 0, "motes": 0}
current_items = input().split()
obtained = False
while not obtained:
    for index in range(0, len(current_items), 2):
        value = int(current_items[index])
        key = current_items[index + 1].lower()
        if key not in items.keys():
            items[key] = 0
        items[key] += value
        if items["shards"] >= 250:
            print("Shadowmourne obtained!")
            items["shards"] -= 250
            obtained = True
        elif items["fragments"] >= 250:
            print("Valanyr obtained!")
            items["fragments"] -= 250
            obtained = True
        elif items["motes"] >= 250:
            print("Dragonwrath obtained!")
            items["motes"] -= 250
            obtained = True
        if obtained:
            break
    if obtained:
        break
    current_items = input().split()
for material, quantity in items.items():
    print(f"{material}: {quantity}")

# 7

parking = {}
number_of_cars = int(input())
for car in range(number_of_cars):
    current_driver = input().split()
    action = current_driver[0]
    if action == "register":
        username = current_driver[1]
        license_plate_number = current_driver[2]
        if username in parking.keys():
            print(f"ERROR: already registered with plate number {license_plate_number}")
        else:
            parking[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
    elif action == "unregister":
        username = current_driver[1]
        if username not in parking.keys():
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del parking[username]
for username, license_plate_number in parking.items():
    print(f"{username} => {license_plate_number}")

# 11

force_side_dictionary = {}
command = input()
while command != "Lumpawaroo":
    if "|" in command:
        splitted_command = command.split(" | ")
        force_side, force_user = splitted_command
        user_is_part_of_the_force = False
        for value in force_side_dictionary.values():
            if force_user in value:  # value is list!!!
                user_is_part_of_the_force = True
                break
        if not user_is_part_of_the_force:
            if force_side not in force_side_dictionary.keys():
                force_side_dictionary[force_side] = [force_user]
            else:
                force_side_dictionary[force_side].append(force_user)
    elif "->" in command:  # else
        splitted_command = command.split(" -> ")
        force_user, force_side = splitted_command
        for key, value in force_side_dictionary.items():
            if force_user in value:  # value is list!!!
                force_side_dictionary[key].pop(value.index(force_user))
                break
        if force_side not in force_side_dictionary.keys():
            force_side_dictionary[force_side] = [force_user]
        else:
            force_side_dictionary[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")
    command = input()
for force_side, force_users in force_side_dictionary.items():
    if len(force_users) > 0:
        print(f"Side: {force_side}, Members: {len(force_users)}")
        for user in force_users:
            print(f"! {user}")
=======
# 1


current_input = input().split()
symbols = ''.join(current_input)
letters = {}
for symbol in symbols:
    if symbol not in letters.keys():
        letters[symbol] = 0
    letters[symbol] += 1
for char, occurrences in letters.items():
    print(f"{char} -> {occurrences}")

# 2


resources = {}
while True:
    current_resource = input()
    if current_resource == "stop":
        break
    current_quantity = int(input())
    if current_resource not in resources.keys():
        resources[current_resource] = 0
    resources[current_resource] += current_quantity
for resource, quantity in resources.items():
    print(f"{resource} -> {quantity}")

# 3

countries = input().split(", ")
capitals = input().split(", ")
final_result = {countries[index]: capitals[index] for index in range(len(countries))}
# final_result = dict(zip(countries, capitals))
for country, capital in final_result.items():
    print(f"{country} -> {capital}")

# 4

phonebook = {}
while True:
    entry = input()
    if "-" not in entry:
        break
    name, phone = entry.split("-")
    phonebook[name] = phone
for check in range(int(entry)):
    searched_name = input()
    if searched_name in phonebook.keys():
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")

# 5

items = {"shards": 0, "fragments": 0, "motes": 0}
current_items = input().split()
obtained = False
while not obtained:
    for index in range(0, len(current_items), 2):
        value = int(current_items[index])
        key = current_items[index + 1].lower()
        if key not in items.keys():
            items[key] = 0
        items[key] += value
        if items["shards"] >= 250:
            print("Shadowmourne obtained!")
            items["shards"] -= 250
            obtained = True
        elif items["fragments"] >= 250:
            print("Valanyr obtained!")
            items["fragments"] -= 250
            obtained = True
        elif items["motes"] >= 250:
            print("Dragonwrath obtained!")
            items["motes"] -= 250
            obtained = True
        if obtained:
            break
    if obtained:
        break
    current_items = input().split()
for material, quantity in items.items():
    print(f"{material}: {quantity}")

# 7

parking = {}
number_of_cars = int(input())
for car in range(number_of_cars):
    current_driver = input().split()
    action = current_driver[0]
    if action == "register":
        username = current_driver[1]
        license_plate_number = current_driver[2]
        if username in parking.keys():
            print(f"ERROR: already registered with plate number {license_plate_number}")
        else:
            parking[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
    elif action == "unregister":
        username = current_driver[1]
        if username not in parking.keys():
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del parking[username]
for username, license_plate_number in parking.items():
    print(f"{username} => {license_plate_number}")

# 11

force_side_dictionary = {}
command = input()
while command != "Lumpawaroo":
    if "|" in command:
        splitted_command = command.split(" | ")
        force_side, force_user = splitted_command
        user_is_part_of_the_force = False
        for value in force_side_dictionary.values():
            if force_user in value:  # value is list!!!
                user_is_part_of_the_force = True
                break
        if not user_is_part_of_the_force:
            if force_side not in force_side_dictionary.keys():
                force_side_dictionary[force_side] = [force_user]
            else:
                force_side_dictionary[force_side].append(force_user)
    elif "->" in command:  # else
        splitted_command = command.split(" -> ")
        force_user, force_side = splitted_command
        for key, value in force_side_dictionary.items():
            if force_user in value:  # value is list!!!
                force_side_dictionary[key].pop(value.index(force_user))
                break
        if force_side not in force_side_dictionary.keys():
            force_side_dictionary[force_side] = [force_user]
        else:
            force_side_dictionary[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")
    command = input()
for force_side, force_users in force_side_dictionary.items():
    if len(force_users) > 0:
        print(f"Side: {force_side}, Members: {len(force_users)}")
        for user in force_users:
            print(f"! {user}")
>>>>>>> 36496de6931529b811d0c463d6ad38e232c5703a
        # [print(f"! {user}") for user in force_side_dictionary[force_side]]