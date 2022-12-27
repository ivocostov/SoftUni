orders_count = int(input())

total_orders_price = 0

for current_order in range(orders_count):
    capsule_price = float(input())
    number_of_days = int(input())
    capsules_per_day = int(input())

    if capsule_price < 0.01 or capsule_price > 100 \
        or number_of_days < 1 or number_of_days > 31 \
            or capsules_per_day < 1 or capsules_per_day > 2000:
        continue
    else:
        order_price = capsule_price * number_of_days * capsules_per_day
        total_orders_price += order_price
        print(f'The price for the coffee is: ${order_price:.2f}')
print(f'Total: ${total_orders_price:.2f}')
