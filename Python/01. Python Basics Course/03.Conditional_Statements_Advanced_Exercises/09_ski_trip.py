number_of_days = int(input())
room_type = input()
opinion = input()
room_price = 0
total_price = 0
number_of_nights = number_of_days - 1

if room_type == "room for one person":
    room_price = 18
elif room_type == "apartment":
    room_price = 25
    if number_of_nights < 10:
        room_price *= 0.7
    elif 10 <= number_of_nights < 15:
        room_price *= 0.65
    elif number_of_nights > 15:
        room_price *= 0.5
elif room_type == "president apartment":
    room_price = 35
    if number_of_nights < 10:
        room_price *= 0.9
    elif 10 <= number_of_nights < 15:
        room_price *= 0.85
    elif number_of_nights > 15:
        room_price *= 0.8

total_price = number_of_nights * room_price

if opinion == "positive":
    total_price *= 1.25
elif opinion == "negative":
    total_price *= 0.9

print(f"{total_price:.2f}")