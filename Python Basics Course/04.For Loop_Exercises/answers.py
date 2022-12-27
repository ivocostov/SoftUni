# 1

for number in range(1, 1000 + 1):
    if number % 10 == 7:
        print(number)

# 2

import sys

count_of_numbers = int(input())
sum_of_all_elements = 0
max_element = - sys.maxsize
for number in range(count_of_numbers):  # range(1, count_of_numbers + 1)
    current_number = int(input())
    sum_of_all_elements += current_number
    if current_number > max_element:
        max_element = current_number
if max_element == sum_of_all_elements - max_element:
    print("Yes")
    print(f"Sum = {max_element}")
else:
    # разликата между най-големия елемент и сумата на останалите
    difference = abs(max_element - (sum_of_all_elements - max_element))
    print("No")
    print(f"Diff = {difference}")

# 2.1 - without sys.maxsize


count_of_numbers = int(input())
sum_of_all_elements = 0
current_number = int(input())
max_element = current_number
sum_of_all_elements += current_number
for number in range(count_of_numbers - 1):  # range(1, count_of_numbers + 1)
    current_number = int(input())
    sum_of_all_elements += current_number
    if current_number > max_element:
        max_element = current_number
if max_element == sum_of_all_elements - max_element:
    print("Yes")
    print(f"Sum = {max_element}")
else:
    # разликата между най-големия елемент и сумата на останалите
    difference = abs(max_element - (sum_of_all_elements - max_element))
    print("No")
    print(f"Diff = {difference}")

# 3

count_of_numbers = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
for numbers in range(count_of_numbers):  # range(1, count_of_numbers + 1)
    current_number = int(input())
    if current_number < 200:
        p1 += 1  # p1 = p1 + 1
    elif current_number < 400:
        p2 += 1  # p2 = p2 + 1
    elif current_number < 600:
        p3 += 1  # p3 = p3 + 1
    elif current_number < 800:
        p4 += 1
    elif current_number >= 800:  # else
        p5 += 1
p1_percentage = p1 / count_of_numbers * 100
p2_percentage = p2 / count_of_numbers * 100
p3_percentage = p3 / count_of_numbers * 100
p4_percentage = p4 / count_of_numbers * 100
p5_percentage = p5 / count_of_numbers * 100
print(f"{p1_percentage:.2f}%")
print(f"{p2_percentage:.2f}%")
print(f"{p3_percentage:.2f}%")
print(f"{p4_percentage:.2f}%")
print(f"{p5_percentage:.2f}%")

# 4

ages = int(input())
laundry_price = float(input())
price_per_toy = int(input())
total_money = 0
total_toys = 0
current_birthday_money = 0
for current_age in range(1, ages + 1):
    if current_age % 2 == 0:
        current_birthday_money += 10
        total_money += current_birthday_money - 1
    else:  # elif current_age % 2 != 0
        total_toys += 1
total_money += total_toys * price_per_toy
difference = abs(total_money - laundry_price)
if total_money >= laundry_price:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")

# 5

opened_tabs = int(input())
salary = int(input())
for current_tab in range(opened_tabs):
    website_name = input()
    if website_name == "Facebook":
        salary -= 150
    elif website_name == "Instagram":
        salary -= 100
    elif website_name == "Reddit":
        salary -= 50
    if salary <= 0:
        break
if salary > 0:
    print(salary)
else:  # we have lost our salary
    print("You have lost your salary.")

# 6

actor_name = input()
academy_points = float(input())
number_of_jury = int(input())
total_points = academy_points
for current_grade in range(number_of_jury):
    current_jury_name = input()
    current_points = float(input())
    # крайни точки = дължината на името на оценяващия умножено по точките, които дава делено на две
    current_final_points = len(current_jury_name) * current_points / 2
    total_points += current_final_points
    if total_points > 1250.5:
        break
if total_points > 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
else:
    difference = 1250.5 - total_points
    print(f"Sorry, {actor_name} you need {difference:.1f} more!")

# 7

number_of_groups = int(input())
mousalla_climbers = 0
monblan_climbers = 0
kilimandjaro_climbers = 0
k2_climbers = 0
everest_climbers = 0
total_climbers = 0
for current_group in range(number_of_groups):  # range(1, number_of_groups+1)
    current_number_of_climbers = int(input())
    if current_number_of_climbers <= 5:
        mousalla_climbers += current_number_of_climbers
    elif current_number_of_climbers <= 12:
        monblan_climbers += current_number_of_climbers
    elif current_number_of_climbers <= 25:
        kilimandjaro_climbers += current_number_of_climbers
    elif current_number_of_climbers <= 40:
        k2_climbers += current_number_of_climbers
    elif current_number_of_climbers >= 41:  # else:
        everest_climbers += current_number_of_climbers
    total_climbers += current_number_of_climbers
mousalla_percentage = mousalla_climbers / total_climbers * 100
monblan_percentage = monblan_climbers / total_climbers * 100
kilimandjaro_percentage = kilimandjaro_climbers / total_climbers * 100
k2_percentage = k2_climbers / total_climbers * 100
everest_percentage = everest_climbers / total_climbers * 100
print(f"{mousalla_percentage:.2f}%")
print(f"{monblan_percentage:.2f}%")
print(f"{kilimandjaro_percentage:.2f}%")
print(f"{k2_percentage:.2f}%")
print(f"{everest_percentage:.2f}%")

# 8