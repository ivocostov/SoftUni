import re
text = input()

food_items = ''
calories = 0

pattern = r'(\||\#)([a-z A-Z]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1'
result = re.findall(pattern, text)

for food in result:
    calories += int(food[-1])
    food_items += f"Item: {food[1]}, Best before: {food[2]}, Nutrition: {food[3]}\n"

days_to_last = calories // 2000

print(f"You have food to last you for: {days_to_last} days!")
print(food_items)
