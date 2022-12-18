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