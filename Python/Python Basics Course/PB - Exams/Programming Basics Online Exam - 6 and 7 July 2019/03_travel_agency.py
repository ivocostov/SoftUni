name_of_town = input()
holiday_package = input()
is_vip = input()
days_of_stay = int(input())
total_price = 0
price_per_day = 0

if name_of_town == 'Bansko' or name_of_town == 'Borovets':
    if holiday_package == 'noEquipment':
        price_per_day = 80
        total_price = days_of_stay * price_per_day
        if is_vip == 'yes':
            total_price *= 0.95

    elif holiday_package == 'withEquipment':
        price_per_day = 100
        total_price = days_of_stay * price_per_day
        if is_vip == 'yes':
            total_price *= 0.90

elif name_of_town == 'Varna' or name_of_town == 'Burgas':
    if holiday_package == 'noBreakfast':
        price_per_day = 100
        total_price = days_of_stay * price_per_day
        if is_vip == 'yes':
            total_price *= 0.93

    elif holiday_package == 'withBreakfast':
        price_per_day = 130
        total_price = days_of_stay * price_per_day
        if is_vip == 'yes':
            total_price *= 0.88

elif name_of_town != ['Varna', 'Burgas', 'Bansko', 'Borovets'] or holiday_package != ['noEquipment', 'withEquipment', 'noBreakfast', 'withBreakfast']:
    print('Invalid input!')
    exit()

if days_of_stay >= 7:
    total_price -= price_per_day
if days_of_stay < 1:
    print("Days must be positive number!")
else:
    print(f"The price is {total_price:.2f}lv! Have a nice time!")

