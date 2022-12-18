from math import ceil
avg_speed = float(input())
fuel_per_100_km = float(input())
earth_to_moon_distance = 384400

total_km_forth_and_back = 2 * earth_to_moon_distance
time_needed_to_travel = total_km_forth_and_back / avg_speed
total_time_to_spend_in_space = time_needed_to_travel + 3
fuel_needed = fuel_per_100_km * total_km_forth_and_back / 100

print(ceil(total_time_to_spend_in_space))
print(int(fuel_needed))
