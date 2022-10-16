number_of_lines_to_follow = int(input())

tank_capacity_in_lt = 255
poured_water_in_the_tank = 0

for liters_of_water in range(number_of_lines_to_follow):
    current_liters_amount = int(input())

    if tank_capacity_in_lt < current_liters_amount:
        print("Insufficient capacity!")
        continue
    else:
        poured_water_in_the_tank += current_liters_amount
        tank_capacity_in_lt -= current_liters_amount
print(poured_water_in_the_tank)
