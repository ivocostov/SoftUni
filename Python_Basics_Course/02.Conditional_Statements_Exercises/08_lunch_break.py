from math import ceil
series_name = input()
series_time_duration = int(input())
break_time_duration = int(input())

lunch_time_duration = break_time_duration / 8
cigarette_time_duration = break_time_duration / 4
total_lunch_and_cigarette_time = lunch_time_duration + cigarette_time_duration
time_difference = abs(break_time_duration - total_lunch_and_cigarette_time)
time_needed_to_watch_series = abs(time_difference - series_time_duration)

if time_difference >= series_time_duration:
    print(f"You have enough time to watch {series_name} and left with {ceil(time_needed_to_watch_series)} \
minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need {ceil(time_needed_to_watch_series)} \
more minutes.")
