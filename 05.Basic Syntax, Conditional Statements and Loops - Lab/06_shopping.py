budget = int(input())

total_items_price = 0
command = input()
while command != 'End':
    item_price = int(command)
    total_items_price += item_price

    if total_items_price > budget:
        print('You went in overdraft!')
        break

    command = input()

if command == 'End':
    print('You bought everything needed.')
