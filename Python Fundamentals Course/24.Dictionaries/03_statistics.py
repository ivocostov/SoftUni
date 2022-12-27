<<<<<<< HEAD
available_products = {}

while True:

    command = input()
    if command == "statistics":
        break

    product, quantity = command.split(": ")
    if product not in available_products.keys():
        available_products[product] = 0
    available_products[product] += int(quantity)

print("Products in stock:")
for products, quantity in available_products.items():
    print(f"- {products}: {quantity}")
print(f"Total Products: {len(available_products)}")
print(f"Total Quantity: {sum(available_products.values())}")
=======
available_products = {}

while True:

    command = input()
    if command == "statistics":
        break

    product, quantity = command.split(": ")
    if product not in available_products.keys():
        available_products[product] = 0
    available_products[product] += int(quantity)

print("Products in stock:")
for products, quantity in available_products.items():
    print(f"- {products}: {quantity}")
print(f"Total Products: {len(available_products)}")
print(f"Total Quantity: {sum(available_products.values())}")
>>>>>>> 36496de6931529b811d0c463d6ad38e232c5703a
