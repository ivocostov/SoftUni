number_of_inputs = int(input())

first_set = set()
second_set = set()
longest_intersection = set()
temp = set()

for _ in range(number_of_inputs):
    temp.clear()
    first_range, second_range = tuple(x.split(',') for x in input().split('-'))

    for first_sequence in range(int(first_range[0]), int(first_range[-1]) + 1):
        first_set.add(first_sequence)
    for second_sequence in range(int(second_range[0]), int(second_range[1]) + 1):
        second_set.add(second_sequence)

    temp = (first_set.intersection(second_set))
    first_set.clear()
    second_set.clear()

    if len(temp) > len(longest_intersection):
        longest_intersection = temp.copy()

print(f"Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}")