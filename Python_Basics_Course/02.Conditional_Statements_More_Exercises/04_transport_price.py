total_km = int(input())
time_of_day = input()

if total_km >= 100:
    price_using_train = total_km * 0.06
    print(f"{price_using_train:.2f}")

elif total_km >= 20:
    price_using_bus = total_km * 0.09
    print(f"{price_using_bus:.2f}")

elif total_km < 20 and time_of_day == "day":
    price_using_taxi_daylight = 0.7 + total_km * 0.79
    print(f"{price_using_taxi_daylight:.2f}")

elif total_km < 20 and time_of_day == "night":
    price_using_taxi_nighttime = 0.7 + total_km * 0.9
    print(f"{price_using_taxi_nighttime:.2f}")





