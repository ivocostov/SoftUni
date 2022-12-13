user_input = input().split(" ")
products_to_search = input().split()

available_products = {}

for index in range(0, len(user_input), 2):
    key = user_input[index]
    value = int(user_input[index + 1])
    available_products[key] = value

for product in products_to_search:
    if product in available_products.keys():
        quantity = available_products[product]
        print(f"We have {quantity} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
