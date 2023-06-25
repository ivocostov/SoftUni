<<<<<<< HEAD
parking_lot = {}

user_input = int(input())

for _ in range(user_input):
    command = input().split()
    current_command = command[0]

    if current_command == "register":
        if command[1] not in parking_lot.keys():
            username = command[1]
            license_plate_number = command[2]
            parking_lot[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate_number}")

    elif current_command == "unregister":
        username = command[1]
        if username not in parking_lot.keys():
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del parking_lot[username]
for username, license_plate_number in parking_lot.items():
=======
parking_lot = {}

user_input = int(input())

for _ in range(user_input):
    command = input().split()
    current_command = command[0]

    if current_command == "register":
        if command[1] not in parking_lot.keys():
            username = command[1]
            license_plate_number = command[2]
            parking_lot[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate_number}")

    elif current_command == "unregister":
        username = command[1]
        if username not in parking_lot.keys():
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del parking_lot[username]
for username, license_plate_number in parking_lot.items():
>>>>>>> 36496de6931529b811d0c463d6ad38e232c5703a
    print(f"{username} => {license_plate_number}")