import sys

current_input = input()
max_number = -sys.maxsize

while current_input != "Stop":
    number = int(current_input)
    if number > max_number:
        max_number = number
    current_input = input()

print(f"{max_number}")
