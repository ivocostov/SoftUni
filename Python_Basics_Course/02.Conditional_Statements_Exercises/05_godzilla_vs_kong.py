film_budget = float(input())
statists_qty = int(input())
statist_uniform_price = float(input())

decor_price = film_budget * 0.1

total_statist_uniform_price = statists_qty * statist_uniform_price

if statists_qty > 150:
    total_statist_uniform_price *= 0.9

total_money_spend = decor_price + total_statist_uniform_price
difference = abs(film_budget - total_money_spend)
if film_budget < total_money_spend:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
