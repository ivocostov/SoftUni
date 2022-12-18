cover_nylon = int(input())
paint_liters = int(input())
thinner_liters = int(input())
hours = int(input())
bags_price = 0.40

cover_nylon_price_per_square_meter = 1.50
paint_price_per_liter = 14.50
thinner_price_per_liter = 5.00


materials_price = (cover_nylon + 2) * cover_nylon_price_per_square_meter + (paint_liters * 1.1) \
                  * paint_price_per_liter + thinner_liters * thinner_price_per_liter + bags_price
salary = materials_price * 0.30 * hours
total_money_spend = materials_price + salary


print(total_money_spend)


