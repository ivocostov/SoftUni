fishermen_budget = int(input())
season = input()
qty_of_fishermen = int(input())
rent_of_the_boat = 0

if season == 'Spring':
    rent_of_the_boat = 3000
    if qty_of_fishermen <= 6:
        rent_of_the_boat *= 0.9
    elif qty_of_fishermen <= 11:
        rent_of_the_boat *= 0.85
    elif qty_of_fishermen > 12:
        rent_of_the_boat *= 0.75
elif season == 'Summer' or season == 'Autumn':
    rent_of_the_boat = 4200
    if qty_of_fishermen <= 6:
        rent_of_the_boat *= 0.9
    elif qty_of_fishermen <= 11:
        rent_of_the_boat *= 0.85
    elif qty_of_fishermen > 12:
        rent_of_the_boat *= 0.75
elif season == 'Winter':
    rent_of_the_boat = 2600
    if qty_of_fishermen <= 6:
        rent_of_the_boat *= 0.9
    elif qty_of_fishermen <= 11:
        rent_of_the_boat *= 0.85
    elif qty_of_fishermen > 12:
        rent_of_the_boat *= 0.75

are_fishermen_odd_number = qty_of_fishermen % 2 == 0

if are_fishermen_odd_number is True and season != 'Autumn':
    rent_of_the_boat *= 0.95

money_difference = abs(fishermen_budget - rent_of_the_boat)

if fishermen_budget >= rent_of_the_boat:
    print(f"Yes! You have {money_difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {money_difference:.2f} leva.")



