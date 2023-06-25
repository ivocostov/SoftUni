month = input()
number_of_nights = int(input())
studio_price = 0
apartment_price = 0

if month == 'May' or month == 'October':
    studio_price = 50
    apartment_price = 65
    if number_of_nights > 14:
        studio_price *= 0.7
    elif number_of_nights > 7:
        studio_price *= 0.95
elif month == 'June' or month == 'September':
    studio_price = 75.20
    apartment_price = 68.70
    if number_of_nights > 14:
        studio_price *= 0.80
elif month == 'July' or month == 'August':
    studio_price = 76
    apartment_price = 77
if number_of_nights > 14:
    apartment_price *= 0.9


total_sum_for_studio = number_of_nights * studio_price
total_sum_for_apartment = number_of_nights * apartment_price

print(f"Apartment: {total_sum_for_apartment:.2f} lv.")
print(f"Studio: {total_sum_for_studio:.2f} lv.")
