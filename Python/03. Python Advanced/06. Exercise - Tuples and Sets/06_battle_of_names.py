number_of_inputs = int(input())

odd_numbers = set()
even_numbers = set()

for row in range(1, number_of_inputs + 1):
    name = input()
    ascii_sum = 0
    for letter in name:
        ascii_sum += ord(letter)

    result = ascii_sum // row

    if result % 2 == 0:
        even_numbers.add(result)
    else:
        odd_numbers.add(result)

if sum(odd_numbers) == sum(even_numbers):
    set_union = odd_numbers.union(even_numbers)
    print(*set_union, sep=', ')
elif sum(odd_numbers) > sum(even_numbers):
    set_difference = odd_numbers.difference(even_numbers)
    print(*set_difference, sep=', ')
elif sum(odd_numbers) < sum(even_numbers):
    set_symmetric_diff = odd_numbers.symmetric_difference(even_numbers)
    print(*set_symmetric_diff, sep=', ')
