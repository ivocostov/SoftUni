<<<<<<< HEAD
def initial_dictionary(number):
    for _ in range(number):
        command = input().split("<->")
        plant = command[0]
        plant_rarity = command[1]

        plant_dictionary[plant] = {'Rarity': [plant_rarity], 'Rating': []}


user_input = int(input())
plant_dictionary = {}
print(plant_dictionary)

=======
def initial_dictionary(number):
    for _ in range(number):
        command = input().split("<->")
        plant = command[0]
        plant_rarity = command[1]

        plant_dictionary[plant] = {'Rarity': [plant_rarity], 'Rating': []}


user_input = int(input())
plant_dictionary = {}
print(plant_dictionary)

>>>>>>> 36496de6931529b811d0c463d6ad38e232c5703a
initial_dictionary(user_input)