coffee_counter = 0
current_command = input()
while current_command != "END":
    if current_command.lower() == "coding" \
            or current_command.lower() == "dog" \
            or current_command.lower() == "cat" \
            or current_command.lower() == "movie":
        if current_command.islower():
            coffee_counter += 1
        else:
            coffee_counter += 2

    current_command = input()
if coffee_counter > 5:
    print("You need extra sleep")
else:
    print(coffee_counter)
