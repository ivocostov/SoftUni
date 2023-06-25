team_A = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
team_B = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']

#team_A = ["A-" + str(s) for s in range(1, 12)]    #използва се list comprehension като се създава лист в
#team_B = ["B-" + str(s) for s in range(1, 12)]    #комбинация от "А-" и числата от 1 до 11, същото се отнася и за "В-"

fined_players = input().split()      # четат се входните данни, всяко поотделно

game_was_terminated = False          # играта е False защото още никой не я е прекъснал

for player in fined_players:
    if player in team_A:             # проверява дали глобеният или изгонен играч е от team_A или team_B и го премахва от списъка
        team_A.remove(player)        # ако вече са премахнати не прави нищо
    elif player in team_B:
        team_B.remove(player)
    if len(team_A) < 7 or len(team_B) < 7:  # ако някой от отборите остане с по-малко от 7 човека играта прекъсва
        game_was_terminated = True
        break

print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")

if game_was_terminated:              # написано по този начин означава: ако game_was_terminated = True
    print("Game was terminated")
