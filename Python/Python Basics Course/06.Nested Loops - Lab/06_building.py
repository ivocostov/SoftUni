floors_count = int(input())
rooms_count_per_floor = int(input())

rooms_counter = 0
room_name = ''

for diminishing_floor in range(floors_count, 0, -1):
    for flats in range(rooms_count_per_floor):
        room_name = diminishing_floor * 10 + flats

        if diminishing_floor == floors_count:
            room_name = f'L{room_name}'
        elif diminishing_floor % 2 != 0:
            room_name = f'A{room_name}'
        elif diminishing_floor % 2 == 0:
            room_name = f'O{room_name}'
        print(room_name, end=' ')
    print()

