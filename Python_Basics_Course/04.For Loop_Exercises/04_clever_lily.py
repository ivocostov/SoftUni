lily_age = int(input())
laundry_machine_price = float(input())
price_per_toy = int(input())

total_lily_money = 0
birthday_money = 0
toys = 0
total_toys_money = 0
total_birthday_money = 0

for num in range(1, lily_age + 1):
    if num % 2 == 0:
        birthday_money += 10
        total_birthday_money += birthday_money - 1
    else:
        toys = toys + 1

total_toys_money = price_per_toy * toys
total_lily_money = total_toys_money + total_birthday_money
difference = abs(laundry_machine_price - total_lily_money)

if total_lily_money >= laundry_machine_price:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")
