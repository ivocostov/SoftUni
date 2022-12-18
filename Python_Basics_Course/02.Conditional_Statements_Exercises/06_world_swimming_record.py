old_time_record = float(input())
distance_in_meters = float(input())
swim_meter_per_sec = float(input())

delay = distance_in_meters // 15
delay *= 12.5

time_to_swim_the_distance = distance_in_meters * swim_meter_per_sec + delay

if time_to_swim_the_distance < old_time_record:
    print(f"Yes, he succeeded! The new world record is {time_to_swim_the_distance:.2f} seconds.")
seconds_slower = time_to_swim_the_distance - old_time_record
if time_to_swim_the_distance >= old_time_record:
    print(f"No, he failed! He was {seconds_slower:.2f} seconds slower.")

