hour = int(input())
minute = int(input())

time_in_15_min = minute + 15

if time_in_15_min >= 60:
    hour += 1
    time_in_15_min %= 60
if hour == 24:
    hour = 0
elif time_in_15_min == 60:
    time_in_15_min = 0
print(f'{hour}:{time_in_15_min:02d}')
