def add_first(nums, seq_1):
    for current_num in nums:
        if current_num not in seq_1:
            seq_1.add(current_num)
    return seq_1


def add_second(nums, seq_2):
    for current_num in nums:
        if current_num not in seq_2:
            seq_2.add(current_num)
    return seq_2


def remove_first(nums, seq_1):
    for current_num in nums:
        if current_num in seq_1:
            seq_1.discard(current_num)
    return seq_1


def remove_second(nums, seq_2):
    for current_num in nums:
        if current_num in seq_2:
            seq_2.discard(current_num)
    return seq_2


def check_subset(seq_1, seq_2):
    if seq_1.issubset(seq_2) or seq_2.issubset(seq_1):
        return True
    return False


sequence_1 = set(int(x) for x in input().split())
sequence_2 = set(int(x) for x in input().split())
number_of_inputs = int(input())

for _ in range(number_of_inputs):
    command = input().split()
    numbers = [int(num) for num in command if num.isdigit()]
    command_to_execute = ' '.join(word for word in command if word.isalpha())

    if command_to_execute == 'Add First':
        sequence_1 = add_first(numbers, sequence_1)
    elif command_to_execute == 'Add Second':
        sequence_2 = add_second(numbers, sequence_2)
    elif command_to_execute == 'Remove First':
        sequence_1 = remove_first(numbers, sequence_1)
    elif command_to_execute == 'Remove Second':
        sequence_2 = remove_second(numbers, sequence_2)
    elif command_to_execute == 'Check Subset':
        check_subset(sequence_1, sequence_2)
        if check_subset(sequence_1, sequence_2):
            print(True)
        else:
            print(False)

print(*sequence_1, sep=', ')
print(*sequence_2, sep=', ')
