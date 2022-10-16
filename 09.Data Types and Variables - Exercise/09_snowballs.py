number_of_snowballs = int(input())

current_snowball_weight = 0
current_snowball_flight_time = 0
current_snowball_quality = 0
current_snowball_value = 0

for characteristics in range(1, number_of_snowballs + 1):
    weight_of_the_snowball = int(input())
    flight_time_to_target = int(input())
    quality_of_snowball = int(input())

    snowball_value = (weight_of_the_snowball / flight_time_to_target) ** quality_of_snowball
    if snowball_value > current_snowball_value:
        current_snowball_value = snowball_value
        current_snowball_weight = weight_of_the_snowball
        current_snowball_flight_time = flight_time_to_target
        current_snowball_quality = quality_of_snowball

print(f"{current_snowball_weight} : {current_snowball_flight_time} = {int(current_snowball_value)} ({current_snowball_quality})")