from math import floor
number_of_processors_to_be_manufactured = int(input())
number_of_employees = int(input())
number_of_workdays = int(input())
money_lost = 0
gained_money = 0

total_work_hours = number_of_employees * number_of_workdays * 8
total_processors_made = floor(total_work_hours / 3)
processor_difference = abs(number_of_processors_to_be_manufactured - total_processors_made)

if total_processors_made < number_of_processors_to_be_manufactured:
    money_lost = processor_difference * 110.1
    print(f"Losses: -> {money_lost:.2f} BGN")
else:
    gained_money = processor_difference * 110.1
    print(f"Profit: -> {gained_money:.2f} BGN")
