def initial_dictionary(number):
    for _ in range(number):
        command = input().split("<->")
        plant = command[0]
        plant_rarity = command[1]

        plant_dictionary[plant] = {'Rarity': [plant_rarity], 'Rating': []}


user_input = int(input())
plant_dictionary = {}
print(plant_dictionary)

initial_dictionary(user_input)