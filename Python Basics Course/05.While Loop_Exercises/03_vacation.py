excursion_money = float(input())
money_on_hand = float(input())

enough_money = False
days_passed = 0
spend_money_counter = 0

while money_on_hand < excursion_money:
    action_taken = input()
    money_to_be_spend_saved = float(input())
    days_passed += 1
    if action_taken == 'spend':
        spend_money_counter += 1
        money_on_hand -= money_to_be_spend_saved
        if spend_money_counter == 5:
            print("You can't save the money.")
            print(f"{days_passed}")
    else:
        money_on_hand += money_to_be_spend_saved
        spend_money_counter = 0

    if money_on_hand < 0:
        money_on_hand = 0

if money_on_hand >= excursion_money:
    enough_money = True
    print(f"You saved the money for {days_passed} days.")
