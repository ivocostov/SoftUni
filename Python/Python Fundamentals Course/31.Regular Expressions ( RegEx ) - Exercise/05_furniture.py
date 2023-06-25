<<<<<<< HEAD
import re

total_furniture_cost = 0
furniture_list = []

while True:
    command = input()
    if command == 'Purchase':
        break

    valid_input = r'>>([A-Za-z]*)<<(\d+\.?\d+)\!(\d+)'
    match = re.match(valid_input, command)


    if match:
        item, price, quantity = match.groups()
        total_furniture_cost += float(price) * int(quantity)
        furniture_list.append(item)

print('Bought furniture:')

for furniture in furniture_list:
    print(furniture)
print(f'Total money spend: {total_furniture_cost:.2f}')
=======
import re

total_furniture_cost = 0
furniture_list = []

while True:
    command = input()
    if command == 'Purchase':
        break

    valid_input = r'>>([A-Za-z]*)<<(\d+\.?\d+)\!(\d+)'
    match = re.match(valid_input, command)


    if match:
        item, price, quantity = match.groups()
        total_furniture_cost += float(price) * int(quantity)
        furniture_list.append(item)

print('Bought furniture:')

for furniture in furniture_list:
    print(furniture)
print(f'Total money spend: {total_furniture_cost:.2f}')
>>>>>>> 36496de6931529b811d0c463d6ad38e232c5703a
