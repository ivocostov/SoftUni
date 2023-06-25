from typing import List

from MainProblem.project import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players: List[Player] = []

    def assign_player(self, player: Player):
        if player not in self.players:
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"

        elif player in self.players:
            return f"Player {player.name} is already in the guild."

        elif player.guild != player.NOT_IN_GUILD:
            return f"Player {player.name} is in another guild."


    def kick_player(self, player_name: str):
        try:
            player = next(filter(lambda p: p.name == player_name, self.players))  # p.name взема името на player_name. Това е необходимо,
                                                                                  # защото player_name е стринг и няма инстанция
                                                                                  # а по този начин можем да вземем инстанцията
        except StopIteration:                                                     # next(filter()) ще върне първото намерено съвпадение и ще брейкне
            return f"Player {player_name} is not in the guild."                   # ако извикаме next() без filter() ще върне първото нещо в списъка
                                                                                  # при повторно извикване ще върне второто и т.н.
        self.players.remove(player)
        player.guild = Player.NOT_IN_GUILD
        return f"Player {player_name} has been removed from the guild."


    def guild_info(self):
        guild_info = f"Guild: {self.name}\n"

        for player in self.players:
            guild_info += f"{player.player_info()}\n"

        return guild_info

        # players_info = '\n'.join([p.player_info() for p in self.players])
        #
        # return f"Guild: {self.name}\n" \
        #        f"{players_info}"
