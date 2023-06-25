number_of_commands = int(input())

parking_lot_list = set()

for current_car in range(number_of_commands):
    command, license_plate = input().split(', ')
    if command == 'IN':
        if license_plate not in parking_lot_list:
            parking_lot_list.add(license_plate)
    elif command == 'OUT':
        if license_plate in parking_lot_list:
            parking_lot_list.discard(license_plate)
if parking_lot_list:
    print(*parking_lot_list, sep='\n')
else:
    print('Parking Lot is Empty')

