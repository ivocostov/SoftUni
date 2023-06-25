rows, cols = [int(x) for x in input().split()]

first_and_last_letter = ord('a')

for row in range(first_and_last_letter, first_and_last_letter + rows):
    for col in range(first_and_last_letter, first_and_last_letter + cols):
        print(f"{chr(row)}{chr(row + col - first_and_last_letter)}{chr(row)}", end=' ')
    print()