fuel = input()
amount = float(input())
card = input()

prices = {"Gas": {"No": 0.93, "Yes": 0.93 - 0.08}, "Gasoline": {"No": 2.22, "Yes": 2.22 - 0.18}, \
          "Diesel": {"No": 2.33, "Yes": 2.33 - 0.12}}
print(type(prices))

total = prices[fuel][card] * amount

if 20.0 < amount <= 25.0:
    total -= total * 0.08
elif amount > 25.0:
    total -= total * 0.1

print(f"{total:.2f} lv.")
