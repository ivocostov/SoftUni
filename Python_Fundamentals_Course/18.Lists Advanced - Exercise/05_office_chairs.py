number_of_rooms_in_bc = int(input())

free_chairs = 0
no_chairs = 0

for current_room in range(1, number_of_rooms_in_bc + 1):
    available_chairs, number_of_visitors = input().split()

    difference = len(available_chairs) - int(number_of_visitors)

    if difference < 0:
        no_chairs += difference
        print(f"{abs(difference)} more chairs needed in room {current_room}")

    free_chairs += difference

if no_chairs >= 0:
    print(f"Game On, {free_chairs} free chairs left")
