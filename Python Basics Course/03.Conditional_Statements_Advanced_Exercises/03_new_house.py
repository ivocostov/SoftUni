type_of_flowers = input()
qty_of_flowers = int(input())
budget = int(input())
total_sum = 0

if type_of_flowers == 'Roses':
    total_sum = qty_of_flowers * 5
    if qty_of_flowers > 80:
        total_sum *= 0.9
elif type_of_flowers == 'Dahlias':
    total_sum = qty_of_flowers * 3.8
    if qty_of_flowers > 90:
        total_sum *= 0.85
elif type_of_flowers == 'Tulips':
    total_sum = qty_of_flowers * 2.8
    if qty_of_flowers > 80:
        total_sum *= 0.85
elif type_of_flowers == 'Narcissus':
    total_sum = qty_of_flowers * 3
    if qty_of_flowers < 120:
        total_sum *= 1.15
elif type_of_flowers == 'Gladiolus':
    total_sum = qty_of_flowers * 2.5
    if qty_of_flowers < 80:
        total_sum *= 1.2

money_difference = abs(budget - total_sum)

if budget >= total_sum:
    print(f"Hey, you have a great garden with {qty_of_flowers} {type_of_flowers} and {money_difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {money_difference:.2f} leva more.")
