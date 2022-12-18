fuel_type = input()
fuel_liters = float(input())
club_card_ownership = input()

if fuel_type == 'Gasoline' and club_card_ownership == 'Yes':
    total_fuel_price = fuel_liters * 2.04
elif fuel_type == 'Gasoline' and club_card_ownership == 'No':
    total_fuel_price = fuel_liters * 2.22

elif fuel_type == 'Diesel' and club_card_ownership == 'Yes':
    total_fuel_price = fuel_liters * 2.21
elif fuel_type == 'Diesel' and club_card_ownership == 'No':
    total_fuel_price = fuel_liters * 2.33

elif fuel_type == 'Gas' and club_card_ownership == 'Yes':
    total_fuel_price = fuel_liters * 0.85
elif fuel_type == 'Gas' and club_card_ownership == 'No':
    total_fuel_price = fuel_liters * 0.93

if 20 <= fuel_liters <= 25:
    total_fuel_price *= 0.92
    print(f'{total_fuel_price:.2f} lv.')
elif fuel_liters > 25:
    total_fuel_price *= 0.9
    print(f'{total_fuel_price:.2f} lv.')
else:
    print(f'{total_fuel_price:.2f} lv.')




