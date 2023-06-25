from MainProblem.project import MercedesTeam
from MainProblem.project import RedBullTeam


class F1SeasonApp:

    def __init__(self):
        self.red_bull_team: RedBullTeam or None = None
        self.mercedes_team: MercedesTeam or None = None

    def register_team_for_season(self, team_name: str, budget: int):
        if team_name == "Red Bull":
            self.red_bull_team = RedBullTeam(budget)
            return f"{team_name} has joined the new F1 season."

        elif team_name == "Mercedes":
            self.red_bull_team = MercedesTeam(budget)
            return f"{team_name} has joined the new F1 season."

        else:
            raise ValueError("Invalid team name!")


    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int):
        if not self.red_bull_team or not self.mercedes_team:
            raise Exception("Not all teams have registered for the season.")

        return self.get_race_results(race_name, red_bull_pos, mercedes_pos)


    def get_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int):
        ahead_team = "Red Bull" if red_bull_pos < mercedes_pos else "Mercedes"

        red_bull_revenue = self.red_bull_team.calculate_revenue_after_race(red_bull_pos)
        mercedes_revenue = self.mercedes_team.calculate_revenue_after_race(mercedes_pos)

        return f"Red Bull: {red_bull_revenue}. " \
               f"Mercedes: {mercedes_revenue}. {ahead_team} is ahead at the {race_name} race."


