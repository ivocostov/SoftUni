from math import floor, ceil
magnoliq_qty = int(input())
zumbul_qty = int(input())
roses_qty = int(input())
cactus_qty = int(input())
gift_price = float(input())

total_magnolii_price = magnoliq_qty * 3.25
total_zumbuli_price = zumbul_qty * 4
total_roses_price = roses_qty * 3.5
total_cactuses_price = cactus_qty * 8

total_order_price = total_magnolii_price + total_zumbuli_price + total_roses_price + total_cactuses_price
total_order_price_after_taxes = total_order_price * 0.95
money_difference = abs(gift_price - total_order_price_after_taxes)

if total_order_price_after_taxes >= gift_price:
    print(f"She is left with {floor(money_difference)} leva.")
else:
    print(f"She will have to borrow {ceil(money_difference)} leva.")

