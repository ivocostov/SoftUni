######################################################################
# ЗАДАЧА ЗА НАМИРАНЕ НА БРОЯ НА НУЛИТЕ ИЛИ ЕДИНИЦИТЕ В ДВОИЧНО ЧИСЛО #
######################################################################

number = int(input())
zero_or_one = int(input())

zero_or_one_counter = 0

while number > 0:
    leftover = number % 2           # взима остатъка от делението на number
    if leftover == zero_or_one:     # проверява дали остатъка е равен на зададеното в zero_or_one
        zero_or_one_counter += 1
    number = number // 2            # дели числото целочислено за продължаване на итерацията

if zero_or_one == 0:
    zero_or_one_as_string = "zeroes"
elif zero_or_one == 1:
    zero_or_one_as_string = "ones"

print(f"We have {zero_or_one_counter} {zero_or_one_as_string}.")
