number_of_dog_food_packages = int(input())
number_of_cat_food_packages = int(input())

dog_food_price = 2.50
cat_food_price = 4

sum_needed_for_dog_food = number_of_dog_food_packages * dog_food_price
sum_needed_for_cat_food = number_of_cat_food_packages * cat_food_price

total_sum = sum_needed_for_dog_food + sum_needed_for_cat_food

print(f'{total_sum} lv.')

