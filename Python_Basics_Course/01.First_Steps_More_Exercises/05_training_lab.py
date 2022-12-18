longitude_in_meters = float(input())
width_in_meters = float(input())
corridor_in_meters = 1

hall_width = width_in_meters - corridor_in_meters
hall_columns = longitude_in_meters // 1.2
hall_rows = hall_width // 0.7
working_areas = hall_rows * hall_columns - 1 - 2

print(working_areas)


