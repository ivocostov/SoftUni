def shop_from_grocery_list(*args):
    budget = args[0]
    grocery_list = set(args[1])
    products_and_price = list(args[2:])
    purchased_products = set()

    for product, price in products_and_price:
        if product in grocery_list and product not in purchased_products:
            if budget >= price:
                purchased_products.add(product)
                budget -= price
            else:
                break

    if grocery_list.issubset(purchased_products):
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(str(n) for n in grocery_list if n not in purchased_products)}."


# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola"],
#     ("cola", 5.8),
#     ("tomato", 10.0),
#     ("tomato", 20.45),
# ))

# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola", "chips", "meat"],
#     ("cola", 5.8),
#     ("tomato", 10.0),
#     ("meat", 22),
# ))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))
