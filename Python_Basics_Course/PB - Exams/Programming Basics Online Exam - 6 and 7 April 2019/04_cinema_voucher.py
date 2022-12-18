voucher_price = int(input())

tickets_bought = 0
other_items_bought = 0
available_sum = voucher_price
command = input()

while command != 'End':

    if len(command) > 8:
        first_letter = ord(command[0])
        second_letter = ord(command[1])
        item_price = first_letter + second_letter
        tickets_bought += 1
        available_sum -= item_price
    if len(command) <= 8:
        first_letter = ord(command[0])
        item_price = first_letter
        if item_price > available_sum:
            break
        other_items_bought += 1
        available_sum -= item_price
    command = input()

print(tickets_bought)
print(other_items_bought)
