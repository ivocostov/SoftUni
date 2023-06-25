from collections import deque

chocolates = deque(int(x) for x in input().split(', '))
cups_of_milk = deque(int(x) for x in input().split(', '))

milkshakes = 0

while milkshakes != 5 and chocolates and cups_of_milk:
    piece_of_chocolate = chocolates.pop() if chocolates or not cups_of_milk else 0
    cup_of_milk = cups_of_milk.popleft() if cups_of_milk or not chocolates else 0


    if piece_of_chocolate <= 0 and cup_of_milk <= 0:
        continue
    elif piece_of_chocolate <= 0:
        cups_of_milk.appendleft(cup_of_milk)
        continue
    elif cup_of_milk <= 0:
        chocolates.append(piece_of_chocolate)
        continue
    elif piece_of_chocolate == cup_of_milk:
        milkshakes += 1
    else:
        cups_of_milk.append(cup_of_milk)
        chocolates.append(piece_of_chocolate - 5)

if milkshakes == 5:
    print(f"Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
print(f"Chocolate: {', '.join(str(chocolate) for chocolate in chocolates) or 'empty'}")  # !!!!!!!!!!!!!  Нов начин за принтиране без else

print(f"Milk: {', '.join(str(milk_cup) for milk_cup in cups_of_milk) or 'empty'}")  # !!!!!!!!!!!!  Нов начин за принтиране без else
