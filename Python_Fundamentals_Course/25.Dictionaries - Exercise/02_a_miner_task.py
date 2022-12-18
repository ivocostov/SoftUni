<<<<<<< HEAD
resources = {}

while True:
    command = input()
    if command == "stop":
        break
    current_quantity = int(input())

    if command not in resources.keys():
        resources[command] = 0
    resources[command] += current_quantity

for resource, quantity in resources.items():
    print(f"{resource} -> {quantity}")
=======
resources = {}

while True:
    command = input()
    if command == "stop":
        break
    current_quantity = int(input())

    if command not in resources.keys():
        resources[command] = 0
    resources[command] += current_quantity

for resource, quantity in resources.items():
    print(f"{resource} -> {quantity}")
>>>>>>> 36496de6931529b811d0c463d6ad38e232c5703a
