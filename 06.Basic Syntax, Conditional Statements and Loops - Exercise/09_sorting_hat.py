current_command = input()

while current_command != "Welcome!":
    if current_command == "Voldemort":
        print("You must not speak of that name!")
        exit()
    elif len(current_command) < 5:
        print(f"{current_command} goes to Gryffindor.")
    elif len(current_command) == 5:
        print(f"{current_command} goes to Slytherin.")
    elif len(current_command) == 6:
        print(f"{current_command} goes to Ravenclaw.")
    elif len(current_command) > 6:
        print(f"{current_command} goes to Hufflepuff.")

    current_command = input()
print("Welcome to Hogwarts.")