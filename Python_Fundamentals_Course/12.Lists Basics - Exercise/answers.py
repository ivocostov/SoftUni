# 1

list_of_numbers = input().split()
opposite_numbers = []
for element in list_of_numbers:
    current_number = -int(element)
    opposite_numbers.append(current_number)
print(opposite_numbers)

# 2

factor = int(input())
count = int(input())
list_of_numbers = []
for multiplier in range(1, count + 1):
    list_of_numbers.append(factor * multiplier)
print(list_of_numbers)

# 3

team_a = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
team_b = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']
# team_a = ["A-" + str(s) for s in range(1,12)]
# team_b = ["B-" + str(s) for s in range(1,12)]
players = input().split()
game_was_terminated = False
for player in players:
    if player in team_a:
        team_a.remove(player)
    elif player in team_b:
        team_b.remove(player)
    if len(team_a) < 7 or len(team_b) < 7:
        game_was_terminated = True
        break
print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if game_was_terminated:  # if game_was_terminated == True
    print("Game was terminated")

# 4

money_list = input().split(", ")
# ["1", "2", "3", "4", "5"]
money_list_as_digit = []
for element in money_list:
    money_list_as_digit.append(int(element))
# [1, 2, 3, 4, 5]
number_of_beggars = int(input())
final_sums = []
starting_index = 0
while starting_index < number_of_beggars:
    sum_for_current_beggar = 0
    for current_index in range(starting_index, len(money_list_as_digit), number_of_beggars):
        sum_for_current_beggar += money_list_as_digit[current_index]
    final_sums.append(sum_for_current_beggar)
    starting_index += 1
print(final_sums)

# 5

deck_of_cards = input().split()
number_of_shuffles = int(input())
for shuffle in range(number_of_shuffles):
    final_deck = []
    middle_of_the_deck = len(deck_of_cards) // 2
    left_part = deck_of_cards[0: middle_of_the_deck]
    right_part = deck_of_cards[middle_of_the_deck::]
    for card_index in range(len(left_part)):
        final_deck.append(left_part[card_index])
        final_deck.append(right_part[card_index])
    deck_of_cards = final_deck
print(deck_of_cards)

# 10


events = input().split("|")
total_coins = 100
total_energy = 100
factory_is_open = True
for event in events:
    event_items = event.split("-")
    type_of_event = event_items[0]
    event_value = int(event_items[1])
    if type_of_event == "rest":
        current_energy = total_energy
        total_energy += event_value
        if total_energy > 100:
            total_energy = 100
        gained_energy = total_energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {total_energy}.")
    elif type_of_event == "order":
        if total_energy >= 30:
            total_energy -= 30
            total_coins += event_value
            print(f"You earned {event_value} coins.")
        else:
            total_energy += 50
            print("You had to rest!")

    else:
        if total_coins >= event_value:
            total_coins -= event_value
            print(f"You bought {type_of_event}.")
        else:
            print(f"Closed! Cannot afford {type_of_event}.")
            factory_is_open = False
            break
if factory_is_open:  # if factory_is_open == True
    print("Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")

# Some examples

my_list = [1, 2, 3, 4, "b", "a", "g", 2, 2, 2, 2]
my_letters_list = ["k", "a", "c", "m"]

# my_letters_list.sort(reverse=True)
# print(my_letters_list)
# print(sorted(my_letters_list))


# char = my_list.pop()
# print(my_list)
# print(char)


# my_list.insert(5, "Pesho")
# print(my_list)

# number = my_list.index(2)
# print(number)


# repetition = my_list.count(2)
# print(repetition)