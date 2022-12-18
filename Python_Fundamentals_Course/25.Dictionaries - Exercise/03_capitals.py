<<<<<<< HEAD
countries = input().split(", ")
capitals = input().split(", ")

dictionary = {countries[index]: capitals[index] for index in range(len(countries))}

for key, value in dictionary.items():
    print(f"{key} -> {value}")
=======
countries = input().split(", ")
capitals = input().split(", ")

dictionary = {countries[index]: capitals[index] for index in range(len(countries))}

for key, value in dictionary.items():
    print(f"{key} -> {value}")
>>>>>>> 36496de6931529b811d0c463d6ad38e232c5703a
