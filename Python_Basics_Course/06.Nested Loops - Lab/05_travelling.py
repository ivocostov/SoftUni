travel_destination = input()


while travel_destination != 'End':
    min_budget = float(input())

    saved_money = 0

    while saved_money < min_budget:
        saved_money += float(input())
        if saved_money >= min_budget:
            print(f"Going to {travel_destination}!")

    travel_destination = input()

