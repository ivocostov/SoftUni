actor_name = input()
academy_points = float(input())
jury_members = int(input())

points_given = 0
all_points = 0
total_academy_points = 0

for num in range(jury_members):
    jury_member_name = input()
    points_given = float(input())
    total_given_points = len(jury_member_name) * points_given / 2
    all_points += total_given_points
    total_academy_points = all_points + academy_points
    if total_academy_points > 1250.5:
        break

if total_academy_points > 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_academy_points:.1f}!")
else:
    difference = 1250.5 - total_academy_points
    print(f"Sorry, {actor_name} you need {difference:.1f} more!")

