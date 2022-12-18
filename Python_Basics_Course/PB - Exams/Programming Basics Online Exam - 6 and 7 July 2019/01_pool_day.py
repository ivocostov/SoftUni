from math import ceil
number_of_people = int(input())
entrance_tax = float(input())
chaise_longue_price = float(input())
umbrella_price = float(input())

total_entrance_tax = number_of_people * entrance_tax
total_umbrella_price = (ceil(number_of_people / 2)) * umbrella_price
total_chaise_longue_price = (ceil(number_of_people * 0.75)) * chaise_longue_price
total_sum = total_entrance_tax + total_umbrella_price + total_chaise_longue_price

print(f"{total_sum:.2f} lv.")