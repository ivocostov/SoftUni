countries = input().split(", ")
capitals = input().split(", ")

dictionary = {countries[index]: capitals[index] for index in range(len(countries))}

for key, value in dictionary.items():
    print(f"{key} -> {value}")
