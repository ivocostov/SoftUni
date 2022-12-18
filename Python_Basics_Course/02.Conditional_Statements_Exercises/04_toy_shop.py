money_needed_for_excursion = float(input())
puzzle_qty = int(input())
talking_doll_qty = int(input())
bear_qty = int(input())
mignon_qty = int(input())
toy_truck_qty = int(input())

total_toys_qty = puzzle_qty + talking_doll_qty + bear_qty + mignon_qty + toy_truck_qty
total_toys_price = puzzle_qty * 2.6 + talking_doll_qty * 3 + bear_qty * 4.10 + mignon_qty * 8.20 + toy_truck_qty * 2

if total_toys_qty >= 50:
    total_toys_price *= 0.75

total_toys_price *= 0.9
total_money_gained = abs(money_needed_for_excursion - total_toys_price)

if total_toys_price >= money_needed_for_excursion:
    print(f"Yes! {total_money_gained:.2f} lv left.")
else:
    print(f"Not enough money! {total_money_gained:.2f} lv needed.")