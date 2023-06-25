type_of_beverage = input()
sugar = input()
number_of_beverages = int(input())
beverage_price = 0
beverages_bought = 0
total_sum = 0

if sugar == 'Without':
    if type_of_beverage == 'Espresso':
        beverage_price = number_of_beverages * 0.9
        beverage_price *= 0.65
    elif type_of_beverage == 'Cappuccino':
        beverage_price = number_of_beverages * 1
        beverage_price *= 0.65
    elif type_of_beverage == 'Tea':
        beverage_price = number_of_beverages * 0.5
        beverage_price *= 0.65
if sugar == 'Normal':
    if type_of_beverage == 'Espresso':
        beverage_price = number_of_beverages * 1
    elif type_of_beverage == 'Cappuccino':
        beverage_price = number_of_beverages * 1.2
    elif type_of_beverage == 'Tea':
        beverage_price = number_of_beverages * 0.6
if sugar == 'Extra':
    if type_of_beverage == 'Espresso':
        beverage_price = number_of_beverages * 1.2
    elif type_of_beverage == 'Cappuccino':
        beverage_price = number_of_beverages * 1.6
    elif type_of_beverage == 'Tea':
        beverage_price = number_of_beverages * 0.7

if type_of_beverage == 'Espresso' and number_of_beverages >= 5:
    beverage_price *= 0.75
if beverage_price > 15:
    beverage_price *= 0.8

print(f"You bought {number_of_beverages} cups of {type_of_beverage} for {beverage_price:.2f} lv.")
