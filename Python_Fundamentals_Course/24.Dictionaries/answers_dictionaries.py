# dictionary -> keys  -> keys()
# dictionary -> values -> values()
# dictionary -> items -> items()

# 1

items = input().split()
bakery = {}
for index in range(0, len(items), 2):
    key = items[index]
    value = int(items[index + 1])
    bakery[key] = value
print(bakery)

# 2

items = input().split()
searched_items = input().split()
bakery = {}
for index in range(0, len(items), 2):
    key = items[index]
    value = int(items[index + 1])
    bakery[key] = value
for product in searched_items:
    if product in bakery.keys():
        quantity = bakery[product]
        print(f"We have {quantity} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")

# 3

products = {}
command = input()
while command != "statistics":
    key, value = command.split(": ")
    if key not in products.keys():
        products[key] = 0
    products[key] += int(value)
    command = input()
print("Products in stock:")
for product, quantity in products.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")

# 4

students = {}
command = input().split(":")
while len(command) > 1:
    name, id, course = command[0], command[1], command[2]
    if course not in students.keys():  # if course not in students
        students[course] = []
    students[course].append(f"{name} - {id}")
    command = input().split(":")
searched_course = command[0].replace("_", " ")
for student in students[searched_course]:
    print(student)
# print('\n'.join(students[searched_course]))


# 5

list_of_characters = input().split(", ")
characters = {key: ord(key) for key in list_of_characters}
print(characters)

