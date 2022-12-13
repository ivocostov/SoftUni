initial_energy = int(input())

battles_won = 0

while True:
    current_command = input()
    if current_command == "End of battle":
        print(f"Won battles: {battles_won}. Energy left: {initial_energy}")
        break

    distance_to_enemy = int(current_command)

    if initial_energy >= distance_to_enemy:
        battles_won += 1

    if battles_won % 3 == 0:
        initial_energy += battles_won

    initial_energy -= distance_to_enemy

    if initial_energy < 0:
        initial_energy = 0
        print(f"Not enough energy! Game ends with {battles_won} won battles and {initial_energy} energy")
        break
