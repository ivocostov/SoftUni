hall_rent = int(input())

statues_price = hall_rent * 0.7
catering_price = statues_price * 0.85
sound_price = catering_price * 0.5

total_price = hall_rent + statues_price + catering_price + sound_price

print(f"{total_price:.2f}")
