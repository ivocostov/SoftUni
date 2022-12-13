people_waiting_for_lift = int(input())
lift_current_state = input().split()

wagons = list(map(int, lift_current_state))
total_lift_capacity = 0

for current_index in range(len(wagons)):
    space_available = 4 - wagons[current_index]
    if people_waiting_for_lift >= 4:
        people_waiting_for_lift -= space_available
        wagons[current_index] += space_available
        total_lift_capacity += space_available
    else:
        wagons[current_index] += people_waiting_for_lift

if total_lift_capacity <= people_waiting_for_lift:
    print(f"There isn't enough space! {people_waiting_for_lift} people in a queue!")
    print(' '.join(str(wagon_capacity) for wagon_capacity in wagons))
else:
    print(f"The lift has empty spots!")
    print(' '.join(str(wagon_capacity) for wagon_capacity in wagons))
