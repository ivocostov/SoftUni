projection_type = input()
number_of_rows = int(input())
number_of_columns = int(input())
total_viewers = number_of_rows * number_of_columns
total_income = 0

if projection_type == 'Premiere':
    total_income = total_viewers * 12
elif projection_type == 'Normal':
    total_income = total_viewers * 7.50
elif projection_type == 'Discount':
    total_income = total_viewers * 5

print(f"{total_income:.2f} leva")
