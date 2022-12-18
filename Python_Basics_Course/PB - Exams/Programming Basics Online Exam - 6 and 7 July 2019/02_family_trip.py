available_budget = float(input())
number_of_overnights = int(input())
overnight_price = float(input())
aux_spend_money_percentage = int(input())

aux_spend_money = aux_spend_money_percentage / 100 * available_budget
budget_without_spend_money = available_budget - aux_spend_money

if number_of_overnights > 7:
    overnight_price *= 0.95
    total_overnights_price = number_of_overnights * overnight_price
else:
    total_overnights_price = number_of_overnights * overnight_price

money_left = available_budget - total_overnights_price - aux_spend_money

if money_left >= 0:
    print(f"Ivanovi will be left with {abs(money_left):.2f} leva after vacation.")
else:
    print(f"{abs(money_left):.2f} leva needed.")