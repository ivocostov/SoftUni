quantity_of_decorations = int(input())
days_left_until_christmas = int(input())

needed_money = 0
christmas_spirit = 0

ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15

for current_day in range(1, days_left_until_christmas + 1):
    if current_day % 11 == 0:
        quantity_of_decorations += 2
    if current_day % 2 == 0:
        needed_money += ornament_set_price * quantity_of_decorations
        christmas_spirit += 5
    if current_day % 3 == 0:
        needed_money += (tree_skirt_price + tree_garland_price) * quantity_of_decorations
        christmas_spirit += 13
    if current_day % 5 == 0:
        needed_money += tree_lights_price * quantity_of_decorations
        christmas_spirit += 17
        if current_day % 3 == 0:
            christmas_spirit += 30
    if current_day % 10 == 0:
        christmas_spirit -= 20
        needed_money += tree_skirt_price + tree_garland_price + tree_lights_price
        if current_day == days_left_until_christmas:
            christmas_spirit -= 30

print(f"Total cost: {needed_money}")
print(f"Total spirit: {christmas_spirit}")
