number_of_cities = int(input())

total_profit = 0
is_raining = False

for city in range(1, number_of_cities + 1):
    city_name = input()
    owner_income = float(input())
    owner_expenses = float(input())

    if city % 5 == 0:
        is_raining = True
        owner_income -= owner_income * 0.1

    if is_raining:
        if city % 3 == 0:
            is_raining = False
            break
    if city % 3 == 0:
        owner_expenses += owner_expenses * 0.5

    profit = owner_income - owner_expenses
    total_profit += profit
    print(f"In {city_name} Burger Bus earned {profit:.2f} leva.")
print(f"Burger Bus total profit: {total_profit:.2f} leva.")
