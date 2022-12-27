def min_max_and_sum(input_number):
    minimum_number = min(input_number)
    maximum_number = max(input_number)
    sum_of_all_numbers = sum(input_number)
    return minimum_number, maximum_number, sum_of_all_numbers


user_input = list(map(int, input().split()))

minimum_number, maximum_number, sum_of_all_numbers = min_max_and_sum(user_input)
print(f"The minimum number is {minimum_number}")
print(f"The maximum number is {maximum_number}")
print(f"The sum number is: {sum_of_all_numbers}")
