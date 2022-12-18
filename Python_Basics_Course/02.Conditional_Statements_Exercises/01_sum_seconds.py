first_competitor_time_in_s = int(input())
second_competitor_time_in_s = int(input())
third_competitor_time_in_s = int(input())

sum_of_total_time_in_s = first_competitor_time_in_s + second_competitor_time_in_s + third_competitor_time_in_s
total_time_in_minutes = sum_of_total_time_in_s // 60
total_time_in_s = sum_of_total_time_in_s % 60

if total_time_in_s < 10:
    print(f'{total_time_in_minutes}:0{total_time_in_s}')
else:
    print(f'{total_time_in_minutes}:{total_time_in_s}')
