bakery_product = input()
number_of_ordered_products_price = int(input())
day_of_december = int(input())

if day_of_december <= 15:
    if bakery_product == 'Cake':
        number_of_ordered_products_price *= 24
    elif bakery_product == 'Souffle':
        number_of_ordered_products_price *= 6.66
    elif bakery_product == 'Baklava':
        number_of_ordered_products_price *= 12.6

    number_of_ordered_products_price *= 0.9

elif day_of_december > 15:
    if bakery_product == 'Cake':
        number_of_ordered_products_price *= 28.7
    elif bakery_product == 'Souffle':
        number_of_ordered_products_price *= 9.8
    elif bakery_product == 'Baklava':
        number_of_ordered_products_price *= 16.98

if day_of_december <= 22:
    if 100 <= number_of_ordered_products_price <= 200:
        number_of_ordered_products_price *= 0.85
    elif number_of_ordered_products_price > 200:
        number_of_ordered_products_price *= 0.75

print(f"{number_of_ordered_products_price:.2f}")
