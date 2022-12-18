desirable_club_profit = float(input())
current_club_profit = 0
command = input()
while command != 'Party!':
    number_of_cocktails = int(input())
    cocktail_price = len(command)
    order_price = cocktail_price * number_of_cocktails

    if order_price % 2 != 0:
        order_price *= 0.75

    current_club_profit += order_price

    if current_club_profit >= desirable_club_profit:
        print(f"Target acquired.")
        print(f"Club income - {current_club_profit:.2f} leva.")
        break
    command = input()

if command == 'Party!':
    difference = abs(desirable_club_profit - current_club_profit)
    print(f"We need {difference:.2f} leva more.")
    print(f"Club income - {current_club_profit:.2f} leva.")