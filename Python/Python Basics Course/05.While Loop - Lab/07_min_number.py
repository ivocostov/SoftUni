import sys

current_input = input()
min_number = sys.maxsize

while current_input != "Stop":
    number = int(current_input)
    if number < min_number:
        min_number = number
    current_input = input()

print(f"{min_number}")