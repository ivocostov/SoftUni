# Moving Target
def shoot_func(index, power, targets):
    if 0 <= index < len(targets):
        if targets[index] - power <= 0:
            targets.pop(index)
        else:
            targets[index] -= power

    return targets


def add_func(index, value, targets):
    if 0 <= index < len(targets):
        targets.insert(index, value)
    else:
        print('Invalid placement!')

    return targets


def strike_func(index, radius, targets):
    validator_index = index - radius >= 0 and index + radius < len(targets)

    if validator_index:
        start_target_index = index - radius
        final_target_index = index + radius
        targets = [targets[i] for i in range(len(targets)) if i < start_target_index or i > final_target_index]
    else:
        print("Strike missed!")

    return targets


def moving_target_func(targets):
    while True:
        command = input()

        if command == 'End':
            break

        current_command, first_element, second_element = command.split(' ')

        if current_command == 'Shoot':
            targets = shoot_func(int(first_element), int(second_element), targets)
        elif current_command == 'Add':
            targets = add_func(int(first_element), int(second_element), targets)
        elif current_command == 'Strike':
            targets = strike_func(int(first_element), int(second_element), targets)

    result = '|'.join([str(num) for num in targets])
    print(result)


data = list(map(int, input().split(' ')))
moving_target_func(data)


# 3.    Inventory
def inventory_func(items):
    while True:
        command_data = input()

        if command_data == "Craft!":
            break

        command, product = command_data.split(' - ')

        if command == 'Collect':
            if product not in items:
                items.append(product)

        elif command == 'Drop':
            if product in items:
                items.remove(product)

        #  {old_item}:{new_item} -> split ':' [old_item, new_item]
        elif command == 'Combine Items':
            old_item, new_item = product.split(':')
            if old_item in items:
                old_item_index = items.index(old_item)
                items.insert(old_item_index + 1, new_item)

        elif command == 'Renew':
            if product in items:
                items.remove(product)
                items.append(product)

    print(', '.join(items))


data = input().split(', ')
inventory_func(data)


# 2.    Shoot for the Win
def reduce_values(targets_sequence, index):
    special_value = targets_sequence[index]
    targets_sequence[index] = -1

    for i in range(len(targets_sequence)):
        if targets_sequence[i] == -1:
            continue

        if special_value < targets_sequence[i]:
            targets_sequence[i] -= special_value
        else:
            targets_sequence[i] += special_value

    return targets_sequence


def shoot_for_the_win_func(targets_sequence):
    count_of_shot_targets = 0

    while True:
        command = input()

        if command == 'End':
            break

        index = int(command)

        if 0 <= index < len(targets_sequence) and targets_sequence[index] != -1:
            count_of_shot_targets += 1
            reduce_values(targets_sequence, index)

    convert_target_values_to_string = [str(num) for num in targets_sequence]
    print(f"Shot targets: {count_of_shot_targets} -> {' '.join(convert_target_values_to_string)}")


data = list(map(int, input().split(' ')))
shoot_for_the_win_func(data)

# 1. guinea pig
quantity_food_in_grams = float(input()) * 1000
quantity_hay_in_grams = float(input()) * 1000
quantity_cover_in_grams = float(input()) * 1000
guineas_weight_in_grams = float(input()) * 1000

flag = False

for day in range(1, 31):
    quantity_food_in_grams -= 300

    if day % 2 == 0:
        quantity_hay_in_grams -= quantity_food_in_grams * 0.05

    if day % 3 == 0:
        quantity_cover_in_grams -= guineas_weight_in_grams / 3

    if quantity_food_in_grams <= 0 or quantity_hay_in_grams <= 0 or quantity_cover_in_grams <= 0:
        flag = True
        break

if not flag:
    food, hay, cover = quantity_food_in_grams / 1000, quantity_hay_in_grams / 1000, quantity_cover_in_grams / 1000
    print(f"Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.")
else:
    print(f"Merry must go to the pet store!")