def initial_dictionary(number):
    for _ in range(number):
        command = input().split("<->")
        plant = command[0]
        plant_rarity = command[1]
        if plant not in plant_dictionary:
            plant_dictionary[plant] = {'rarity': plant_rarity, 'rating': []}
        elif plant in plant_dictionary:
            plant_dictionary[plant] = {'rarity': plant_rarity}
    #return plant_dictionary


def rate_function(plant, rating):
    if plant in plant_dictionary.keys():
        if plant_dictionary[plant]['rating'] == [0]:
            plant_dictionary[plant]['rating'] = [int(rating)]
        else:
            plant_dictionary[plant]['rating'].append(int(rating))
    else:
        print("error")
    #return plant_dictionary


def update_function(plant, new_rarity):
    if plant in plant_dictionary.keys():
        plant_dictionary[plant]['rarity'] = new_rarity
    else:
        print("error")
    #return plant_dictionary


def reset_function(plant):
    if plant in plant_dictionary.keys():
        plant_dictionary[plant]['rating'] = []
    else:
        print("error")
    #return plant_dictionary


def discovered_plants(number):
    initial_dictionary(number)

    while True:
        command = input().split(": ")
        if command[0] == "Exhibition":
            break

        action = command[0]
        plant_info = command[1]

        if action == "Rate":
            current_plant_info = plant_info.split(" - ")
            plant = current_plant_info[0]
            rating = int(current_plant_info[1])
            rate_function(plant, rating)
        elif action == "Update":
            current_plant_info = plant_info.split(" - ")
            plant = current_plant_info[0]
            new_rarity = current_plant_info[1]
            update_function(plant, new_rarity)
        elif action == "Reset":
            current_plant_info = plant_info.split(" - ")
            plant = current_plant_info[0]
            reset_function(plant)


    print("Plants for the exhibition:")

    for plants in plant_dictionary.keys():
        rarity = plant_dictionary[plants]['rarity']
        average_rating = 0
        if len(plant_dictionary[plants]['rating']) > 0:
            average_rating = sum(plant_dictionary[plants]['rating']) / len(plant_dictionary[plants]['rating'])
        print(f"- {plants}; Rarity: {rarity}; Rating: {average_rating:.2f}")


user_input = int(input())
plant_dictionary = {}

discovered_plants(user_input)