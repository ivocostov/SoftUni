aqarium_longitude = int(input())
aqarium_width = int(input())
aqarium_height = int(input())
non_water_percent = float(input())

aquarium_volume_in_cm3 = aqarium_longitude * aqarium_width * aqarium_height
aquarium_volume_in_dm3 = aquarium_volume_in_cm3 / 1000
percent_to_value = non_water_percent * 0.01

water_volume_in_liters = aquarium_volume_in_dm3 * (1 - percent_to_value)
print(water_volume_in_liters)