from math import floor

tournaments_qty = int(input())
starting_ranklist_points = int(input())

games_won = 0
total_ranklist_points = starting_ranklist_points

for _ in range(tournaments_qty):
    tournament_stage = input()
    if tournament_stage == "W":
        total_ranklist_points += 2000
        games_won += 1
    elif tournament_stage == "F":
        total_ranklist_points += 1200
    elif tournament_stage == "SF":
        total_ranklist_points += 720

mid_value_points = (total_ranklist_points - starting_ranklist_points) / tournaments_qty
won_games_percentage = games_won / tournaments_qty * 100

print(f"Final points: {total_ranklist_points}")
print(f"Average points: {floor(mid_value_points)}")
print(f"{won_games_percentage:.2f}%")
