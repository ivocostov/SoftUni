from math import floor
group_size = int(input())
number_of_days = int(input())

coins_counter = 0

for day in range(1, number_of_days + 1):
    coins_counter += 50

    if day % 10 == 0:
        group_size -= 2
    if day % 15 == 0:
        group_size += 5
    if day % 3 == 0:
        coins_counter -= group_size * 3
    if day % 5 == 0:
        coins_counter += group_size * 20
        if day % 3 == 0:
            coins_counter -= group_size * 2

    coins_counter -= group_size * 2

coins_per_companion = coins_counter / group_size

print(f"{group_size} companions received {floor(coins_per_companion)} coins each.")
