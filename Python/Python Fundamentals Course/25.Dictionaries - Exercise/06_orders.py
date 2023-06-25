<<<<<<< HEAD
orders_dictionary = {}

while True:
    command = input()
    if command == "buy":
        break

    name, price, quantity = command.split()
    if name not in orders_dictionary.keys():
        orders_dictionary[name] = []
        orders_dictionary[name] = [float(price), int(quantity)]
    else:
        orders_dictionary[name][0] = float(price)
        orders_dictionary[name][1] += int(quantity)

for product_name, price in orders_dictionary.items():
    total_price = orders_dictionary[product_name][0] * orders_dictionary[product_name][1]
    print(f"{product_name} -> {total_price:.2f}")

=======
orders_dictionary = {}

while True:
    command = input()
    if command == "buy":
        break

    name, price, quantity = command.split()
    if name not in orders_dictionary.keys():
        orders_dictionary[name] = []
        orders_dictionary[name] = [float(price), int(quantity)]
    else:
        orders_dictionary[name][0] = float(price)
        orders_dictionary[name][1] += int(quantity)

for product_name, price in orders_dictionary.items():
    total_price = orders_dictionary[product_name][0] * orders_dictionary[product_name][1]
    print(f"{product_name} -> {total_price:.2f}")

>>>>>>> 36496de6931529b811d0c463d6ad38e232c5703a
