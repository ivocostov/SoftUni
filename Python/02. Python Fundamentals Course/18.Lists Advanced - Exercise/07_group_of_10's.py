sequence_of_numbers = list(map(int, input().split(', ')))

group_boundary = 10

while True:
    current_group = []
    for current_number in sequence_of_numbers:
        if current_number <= group_boundary:
            current_group.append(current_number)
    print(f"Group of {group_boundary}'s: {current_group}")
    [[sequence_of_numbers.remove(num) for num in sequence_of_numbers if num == num_current_group]
     for num_current_group in current_group]

    group_boundary += 10
    if len(sequence_of_numbers) == 0:
        break
