peter_budget = float(input())
video_cards_qty = int(input())
cpu_qty = int(input())
ram_memory_qty = int(input())

video_card_price = 250
total_purchased_video_cards = video_cards_qty * video_card_price
cpu_price = total_purchased_video_cards * 0.35
ram_memory_price = total_purchased_video_cards * 0.1

peter_needed_amount_of_money = total_purchased_video_cards + cpu_qty * cpu_price + ram_memory_qty * ram_memory_price

if video_cards_qty > cpu_qty:
    peter_needed_amount_of_money *= 0.85

difference = abs(peter_needed_amount_of_money - peter_budget)

if peter_budget >= peter_needed_amount_of_money:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")
