sequence_of_cards = input().split()
count_of_shuffles = int(input())

for shuffle in range(count_of_shuffles):
    shuffled_cards = []
    middle_of_the_cards_sequence = len(sequence_of_cards) // 2
    left_part_of_the_cards = sequence_of_cards[:middle_of_the_cards_sequence]
    right_part_of_the_cards = sequence_of_cards[middle_of_the_cards_sequence::]
    for card_index in range(len(left_part_of_the_cards)):
        shuffled_cards.append(left_part_of_the_cards[card_index])
        shuffled_cards.append(right_part_of_the_cards[card_index])

    sequence_of_cards = shuffled_cards

print(sequence_of_cards)
