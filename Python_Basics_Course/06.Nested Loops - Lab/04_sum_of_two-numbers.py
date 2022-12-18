first_number = int(input())
second_number = int(input())
magic_number = int(input())

combinations_equal_to_magic_number = 0
combination_flag = False

for num_1 in range(first_number, second_number + 1):
    for num_2 in range(first_number, second_number + 1):
        combinations_equal_to_magic_number += 1
        if num_1 + num_2 == magic_number:
            combination_flag = True
            print(f"Combination N:{combinations_equal_to_magic_number} ({num_1} + {num_2} = {magic_number})")
            break
    if combination_flag:
        break
if not combination_flag:
    print(f"{combinations_equal_to_magic_number} combinations - neither equals {magic_number}")
