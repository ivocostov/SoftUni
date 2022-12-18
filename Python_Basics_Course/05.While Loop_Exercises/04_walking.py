steps_goal = 10000
steps_counter = 0

while steps_counter < steps_goal:
    command = input()
    if command == 'Going home':
        daily_steps_walked = int(input())
        steps_counter += daily_steps_walked
        break
    current_daily_steps = int(command)
    steps_counter += current_daily_steps
difference = abs(steps_counter - steps_goal)

if steps_counter >= steps_goal:
    print("Goal reached! Good job!")
    print(f"{difference} steps over the goal!")
else:
    print(f"{difference} more steps to reach goal.")



