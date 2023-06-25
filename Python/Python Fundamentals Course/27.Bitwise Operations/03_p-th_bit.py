<<<<<<< HEAD
user_number = int(input())
bit_position = int(input())

binary_number = bin(user_number).replace("0b", "")

find_bit = user_number >> bit_position

result = find_bit & bit_position

print(result)
=======
user_number = int(input())
bit_position = int(input())

binary_number = bin(user_number).replace("0b", "")

find_bit = user_number >> bit_position

result = find_bit & bit_position

print(result)
>>>>>>> 36496de6931529b811d0c463d6ad38e232c5703a
