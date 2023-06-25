def sum_numbers(first_num, second_num):
    return first_num + second_num


def subtract(first_function_sum, third_num):
    return first_function_sum - third_num


def add_and_subtract(first_num, second_num, third_num):
    first_and_second_sum = sum_numbers(first_num, second_num)
    answer = subtract(first_and_second_sum, third_num)
    return answer


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(add_and_subtract(first_number, second_number, third_number))
