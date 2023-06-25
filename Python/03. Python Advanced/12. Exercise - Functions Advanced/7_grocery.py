def grocery_store(**kwargs):
    sorted_groceries = sorted(kwargs.items(), key=lambda n: (-n[1], -len(n[0]), n[0]))

    products_list = []

    for product, quantity in sorted_groceries:
        products_list.append(f"{product}: {quantity}")

    return '\n'.join(str(el) for el in products_list)


# print(grocery_store(
#     bread=5,
#     pasta=12,
#     eggs=12,
#
# ))


print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
