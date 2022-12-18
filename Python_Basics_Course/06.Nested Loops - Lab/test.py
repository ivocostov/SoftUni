command = input()

while command != "End":
    budget = float(input())

    saved_money = 0
    total_saved_money = 0

    while saved_money < budget:
        saved_money += float(input())
        if saved_money >= budget:
            print(f"Going to {command}!")

    command = input()
