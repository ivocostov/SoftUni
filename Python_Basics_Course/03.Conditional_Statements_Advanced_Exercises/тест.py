month = input()
number_of_nights = int(input())
apartment_price = 0
studio_price = 0

if month == 'May' and month == 'October':
    studio_price = 50
    apartment_price = 65
    if number_of_nights > 14:
        studio_price *= 0.70
    elif number_of_nights > 7:
        studio_price *= 0.95
elif month == 'June' and month == 'September':
    studio_price = 75.20
    apartment_price = 68.70
    if number_of_nights > 14:
        studio_price *= 0.80
elif month == 'July' and month == 'August':
    studio_price = 76
    apartment_price = 77
if number_of_nights > 14:
    apartment_price *= 0.90

total_studio_price = number_of_nights * studio_price
total_apartment_price = number_of_nights * apartment_price

print(f"Apartment: {total_apartment_price:.2f} lv.")
print(f"Studio: {total_studio_price:.2f} lv.")