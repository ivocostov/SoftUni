user_number = int(input())
bit_position = int(input())

binary_number = bin(user_number).replace("0b", "")

find_bit = user_number >> bit_position

result = find_bit & bit_position

print(result)
