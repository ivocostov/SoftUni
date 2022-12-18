<<<<<<< HEAD
# decimal_number = int(input())
#
# binary_number = []
#
# while decimal_number > 0:
#     remainder = decimal_number % 2
#     binary_number.append(remainder)
#     decimal_number = decimal_number // 2
#
# binary_number = binary_number[::-1]
# print(binary_number[-2])


decimal_number = int(input())
bit_at_position_1 = 1

bit_value = decimal_number >> bit_at_position_1  # измества надясно битовете с n позиции до бит позиция 1

result = bit_value & 1    # проверява каква стойност има бита на позиция едно (единица или нула) и го извежда
print(result)
=======
# decimal_number = int(input())
#
# binary_number = []
#
# while decimal_number > 0:
#     remainder = decimal_number % 2
#     binary_number.append(remainder)
#     decimal_number = decimal_number // 2
#
# binary_number = binary_number[::-1]
# print(binary_number[-2])


decimal_number = int(input())
bit_at_position_1 = 1

bit_value = decimal_number >> bit_at_position_1  # измества надясно битовете с n позиции до бит позиция 1

result = bit_value & 1    # проверява каква стойност има бита на позиция едно (единица или нула) и го извежда
print(result)
>>>>>>> 36496de6931529b811d0c463d6ad38e232c5703a
