def shopping_cart(*args):
    inventory = {'Soup': [], 'Pizza': [], 'Dessert': []}
    inventory_limit = {'Soup': 3, 'Pizza': 4, 'Dessert': 2}
    adding_condition = False

    for current_data in args:
        if current_data == 'Stop':
            break

        meal, meal_product = current_data

        if meal in inventory and meal_product not in inventory[meal]:
            if len(inventory[meal]) < inventory_limit[meal]:
                adding_condition = True
                inventory[meal].append(meal_product)



    if adding_condition:
        output = ''
        sorted_data = sorted(inventory, key=lambda k: (-len(inventory[k]), k))

        for key in sorted_data:
            output += f'{key}:\n'
            for element in sorted(inventory[key]):
                output += f'- {element}\n'

        return output






print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
