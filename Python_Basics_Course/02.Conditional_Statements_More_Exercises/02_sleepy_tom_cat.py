vacation_days = int(input())

year_in_days = 365
toms_play_norm_in_min = 30000

daily_play_with_tom_when_at_work = 63
daily_play_with_tom_when_in_vacation = 127

working_days = year_in_days - vacation_days
real_play_time_at_work_days = working_days * daily_play_with_tom_when_at_work
real_play_time_at_vacation_days = vacation_days * daily_play_with_tom_when_in_vacation
total_real_play_time = real_play_time_at_work_days + real_play_time_at_vacation_days

difference_in_play_time_when_at_work_in_min = abs(toms_play_norm_in_min - total_real_play_time)

play_time_in_hours = difference_in_play_time_when_at_work_in_min // 60
play_time_in_min = difference_in_play_time_when_at_work_in_min % 60

if total_real_play_time > toms_play_norm_in_min:
    print('Tom will run away')
    print(f"{play_time_in_hours} hours and {play_time_in_min} minutes more for play")
else:
    print('Tom sleeps well')
    print(f"{play_time_in_hours} hours and {play_time_in_min} minutes less for play")
