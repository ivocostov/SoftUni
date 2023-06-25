from collections import deque

number_of_petrol_pumps = int(input())
gas_in_truck_tank = 0
pump_index = 0

pump_info = deque([int(x) for x in input().split()] for pump in range(number_of_petrol_pumps))
copy_of_pump_info = pump_info.copy()

while copy_of_pump_info:
    fuel_amount, distance = copy_of_pump_info.popleft()
    gas_in_truck_tank += fuel_amount
    if gas_in_truck_tank >= distance:
        gas_in_truck_tank -= distance

    else:
        pump_info.rotate(-1)
        copy_of_pump_info = pump_info.copy()
        gas_in_truck_tank = 0
        pump_index += 1

print(pump_index)
