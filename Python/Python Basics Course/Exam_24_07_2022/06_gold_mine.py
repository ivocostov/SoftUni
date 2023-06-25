number_of_locations = int(input())

for num in range(1, number_of_locations + 1):
    avg_daily_gold_qty_mined = float(input())
    location_workdays = int(input())
    total_gold_mined = 0
    for day in range(1, location_workdays + 1):
        mined_gold_for_the_day = float(input())
        total_gold_mined += mined_gold_for_the_day

    avg_qty_for_days_in_location = total_gold_mined / location_workdays

    if avg_qty_for_days_in_location >= avg_daily_gold_qty_mined:
        print(f"Good job! Average gold per day: {avg_qty_for_days_in_location:.2f}.")
    else:
        difference_in_gold_qty = abs(avg_daily_gold_qty_mined - avg_qty_for_days_in_location)
        print(f"You need {difference_in_gold_qty:.2f} gold.")

