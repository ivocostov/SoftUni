#1

from math import floor

series_name = input()
number_of_seasons = int(input())
number_of_episodes = int(input())
episode_time_duration = float(input())

commercials_time_duration = episode_time_duration * 0.2

total_episode_time_duration = episode_time_duration + commercials_time_duration
total_episodes = number_of_episodes * number_of_seasons
last_episodes_time_duration = number_of_seasons * 10
total_episodes_time_in_min = total_episodes * total_episode_time_duration + last_episodes_time_duration

print(f"Total time needed to watch the {series_name} series is {floor(total_episodes_time_in_min)} minutes.")


#2

minutes_of_control = int(input())
seconds_of_control = int(input())
lenght_of_shute_in_meters = float(input())
seconds_to_go_100_meters = int(input())

control_in_seconds = minutes_of_control * 60 + seconds_of_control
number_of_time_reduction = lenght_of_shute_in_meters / 120
total_time_reduction = number_of_time_reduction * 2.5

competitor_time = lenght_of_shute_in_meters / 100 * seconds_to_go_100_meters -total_time_reduction

if control_in_seconds >= competitor_time:
    print(f"Marin Bangiev won an Olympic quota!\n His time is {competitor_time}.")
else:
    print(f"No, Marin failed! He was {abs(control_in_seconds - competitor_time)} second slower.")


#3

size_of_eggs = input()
color_of_eggs = input()
number_of_batch = int(input())

total_sum = 0

if size_of_eggs == 'Large':
    if color_of_eggs == 'Red':
        total_sum = number_of_batch * 16
    elif color_of_eggs == 'Green':
        total_sum = number_of_batch * 12
    elif color_of_eggs == 'Yellow':
        total_sum = number_of_batch * 9
elif size_of_eggs == 'Medium':
    if color_of_eggs == 'Red':
        total_sum = number_of_batch * 13
    elif color_of_eggs == 'Green':
        total_sum = number_of_batch * 9
    elif color_of_eggs == 'Yellow':
        total_sum = number_of_batch * 7
elif size_of_eggs == 'Small':
    if color_of_eggs == 'Red':
        total_sum = number_of_batch * 9
    elif color_of_eggs == 'Green':
        total_sum = number_of_batch * 8
    elif color_of_eggs == 'Yellow':
        total_sum = number_of_batch * 5

taxes = total_sum * 0.35
total_sum -= taxes
print(f"{total_sum:.2f} leva.")


#4

number_of_balls = int(input())

red, orange, yellow, white, black, others = 0, 0, 0, 0, 0, 0
total_points = 0

for _ in range(number_of_balls):
    current_color = input()

    if current_color == 'red':
        red += 1
        total_points += 5
    elif current_color == 'orange':
        orange += 1
        total_points += 10
    elif current_color == 'yellow':
        yellow += 1
        total_points += 15
    elif current_color == 'white':
        white += 1
        total_points += 20
    elif current_color == 'black':
        black += 1
        total_points = int(total_points / 2)
    else:
        others += 1

print(f"Total points: {total_points}")
print(f"Red balls: {red}")
print(f"Orange balls: {orange}")
print(f"Yellow balls: {yellow}")
print(f"White balls: {white}")
print(f"Other colors picked: {others}")
print(f"Divides from black balls: {black}")


#5


available_food = int(input()) * 1000

while True:
    command = input()

    if command == 'Adopted':
        break

    current_portion = int(command)
    available_food -= current_portion

if available_food >= 0:
    print(f"Food is enough! Leftovers: {available_food} grams.")
else:
    print(f"Food is not enough. You need {abs(available_food)} grams more.")


#6


number_of_easter_breads = int(input())

best_baker_name = ''
best_baker_score = 0

for count in range(number_of_easter_breads):
    name_of_baker = input()
    current_score = 0

    while True:
        command = input()
        if command == 'Stop':
            print(f"{name_of_baker} has {current_score} points.")
            break
        points = int(input())
        current_score += points

    if current_score > best_baker_score:
        best_baker_score = current_score
        best_baker_name = name_of_baker
        print(f"{name_of_baker} is the new number 1!")

print(f"{best_baker_name} won competition with {best_baker_score} points!")


#7 PB Exams 18 - 19 July 2020 - Task: Barcode Generator


first_number = input()
second_number = input()

for num_1 in range(int(first_number[0]), int(second_number[0]) + 1):
    for num_2 in range(int(first_number[1]), int(second_number[1]) + 1):
        for num_3 in range(int(first_number[2]), int(second_number[2]) + 1):
            for num_4 in range(int(first_number[3]), int(second_number[3]) + 1):
                if num_1 % 2 != 0 and num_2 % 2 != 0 and num_3 % 2 != 0 and num_4 % 2 != 0:
                    print(f"{num_1}{num_2}{num_3}{num_4}", end=' ')



#8 PB Exams 6 - 7 July 2019 - Task: Name Game

best_name = ''
final_sum = 0

while True:
    command = input()
    current_sum = 0
    if command == 'Stop':
        break

    name = command

    for ch in name:
        current_num = int(input())
        if current_num == ord(ch):
            current_sum += 10
        else:
            current_num += 2
    if current_sum >= final_sum:
        final_sum = current_sum
        best_name = name
