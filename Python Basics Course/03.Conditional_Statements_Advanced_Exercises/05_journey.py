programmer_budget = float(input())
possible_season = input()
money_spent = 0
destination = ""
type_of_vacation = ""

if programmer_budget <= 100 and possible_season == 'summer':
    money_spent = programmer_budget * 0.3
    destination = 'Bulgaria'
    type_of_vacation = 'Camp'
elif programmer_budget <= 100 and possible_season == 'winter':
    money_spent = programmer_budget * 0.7
    destination = 'Bulgaria'
    type_of_vacation = 'Hotel'
elif programmer_budget <= 1000 and possible_season == 'summer':
    money_spent = programmer_budget * 0.4
    destination = 'Balkans'
    type_of_vacation = 'Camp'
elif programmer_budget <= 1000 and possible_season == 'winter':
    money_spent = programmer_budget * 0.8
    destination = 'Balkans'
    type_of_vacation = 'Hotel'
elif programmer_budget > 1000:
    money_spent = programmer_budget * 0.9
    destination = 'Europe'
    type_of_vacation = 'Hotel'

print(f"Somewhere in {destination}")
print(f"{type_of_vacation} - {money_spent:.2f}")
