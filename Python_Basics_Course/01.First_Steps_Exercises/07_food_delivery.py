chicken_menu_count = int(input())
fish_menu_count = int(input())
vegetarian_menu_count = int(input())

chicken_menu_price = 10.35
fish_menu_price = 12.40
vegetarian_menu_price = 8.15
delivery_price = 2.50

sum_for_order = chicken_menu_count * chicken_menu_price + fish_menu_count * fish_menu_price + vegetarian_menu_count \
                * vegetarian_menu_price

desert_price = sum_for_order * 0.2
total_price = sum_for_order + desert_price + delivery_price
print(total_price)