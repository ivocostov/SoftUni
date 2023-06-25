def orders(drink_type, quantity):
    total_bill = 0
    if type_of_drink == 'coffee':
        total_bill = qty_of_drink * 1.5
    elif type_of_drink == 'coke':
        total_bill = qty_of_drink * 1.4
    elif type_of_drink == 'water':
        total_bill = qty_of_drink * 1
    elif type_of_drink == 'snacks':
        total_bill = qty_of_drink * 2
    return total_bill


type_of_drink = input()
qty_of_drink = int(input())
final_bill = orders(type_of_drink, qty_of_drink)
print(f'{final_bill:.2f}')