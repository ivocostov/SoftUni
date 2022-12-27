def perfect_number(number):
    #number_is_perfect = True
    sum_of_numbers = 0
    for index in range(1, number):
        if number % index == 0:
            sum_of_numbers += index
    if sum_of_numbers == number:
        return "We have a perfect number!"
    return "It's not so perfect."
        #number_is_perfect = True
    #elif sum_of_numbers != number:
        #number_is_perfect = False
    #return number_is_perfect


user_input = int(input())
#num_is_perfect = perfect_number(user_input)
print(perfect_number(user_input))
#if num_is_perfect:
    #print("We have a perfect number!")
#else:
    #print("It's not so perfect.")
