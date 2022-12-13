"""
You are a pro MOBA player, you are struggling to become а master of the Challenger tier. So, you carefully watch the
statistics in the tier.
You will receive several input lines in one of the following formats:
"{player} -> {position} -> {skill}"
"{player} vs {player}"
The "player" and "position" are strings, and the given "skill" will be an integer number. You need to keep track of
every player.
When you receive a player with his position and skill, add him to the players' pool, if he isn`t present, else add
his position and skill or update his skill, only if the current position skill is lower than the new value.
If you receive "{player} vs {player}" and both players exist in the tier, they duel with the following rules:

•	If they got at least one position in common, the player with better total skill points wins and the other is
    demoted from the tier -> remove him.
•	If they have same total skill points at the same positions, the duel is tie and they both continue in the Season.
•	If they don`t have positions in common, the duel isn`t happening and both continue in the Season.

You should end your program when you receive the command "Season end". At that point you should print the players,
ordered by total skill in descending order, then ordered by player name in ascending order. For each player print their
position and skill, ordered descending by skill, then ordered by position name in ascending order.
"""

players_dictionary = {}


def players_duel(player_1, player_2):
    if player_1 in players_dictionary.keys() and player_2 in players_dictionary.keys():
        for player_position, skill_points in players_dictionary[player_1].items():
            if player_position in players_dictionary[player_2].keys():
                player_1_skill_points = players_dictionary[player_1][position]
                player_2_skill_points = players_dictionary[player_2][position]
                if player_1_skill_points < player_2_skill_points:
                    players_dictionary.pop(player_1)
                elif player_2_skill_points < player_1_skill_points:
                    players_dictionary.pop(player_2)


def show_results():
    total_points = {users: sum(players_dictionary[users].values()) for users in players_dictionary.keys()}
    for user, score in sorted(total_points.items(), key=lambda x: (-x[1], x[0])):
        print(f"{user}: {score} skill")
        for current_position, current_skill in sorted(players_dictionary[user].items(), key=lambda x: (-x[1], x[0])):
            print(f"- {current_position} <::> {current_skill}")


while True:
    user_input = input()
    if user_input == 'Season end':
        break
    elif 'vs' in user_input:
        duel = user_input.split(" vs ")
        first_player = duel[0]
        second_player = duel[-1]
        players_duel(first_player, second_player)
    else:
        player, position, skill = [int(x) if x.isdigit() else x for x in user_input.split(' -> ')]

        players_dictionary[player] = players_dictionary.get(player, {})
        players_dictionary[player][position] = players_dictionary[player].get(position, 0)
        if players_dictionary[player][position] < skill:
            players_dictionary[player][position] = skill

show_results()
