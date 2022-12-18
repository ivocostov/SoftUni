film_budget = float(input())
statists_qty = int(input())
statists_outfit_price = float(input())
decor_price = film_budget * 0.1
expenses = 0

if statists_qty >= 150:
    statists_outfit_price *= 0.9

all_statists_outfit_price = statists_qty * statists_outfit_price
expenses = decor_price + all_statists_outfit_price

difference = abs(film_budget - expenses)

if film_budget >= expenses:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")







