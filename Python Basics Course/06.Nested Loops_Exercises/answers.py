# 1

number = int(input())
counter = 1
all_is_printed = False
for row in range(1, number + 1):
    for column in range(1, row + 1):
        print(counter, end=" ")
        counter += 1
        if counter > number:
            all_is_printed = True
            break
    if all_is_printed:  # if all_is_printed == True
        break
    print()

# 2

first_number = int(input())
second_number = int(input())
for current_number in range(first_number, second_number + 1):
    even_digit_sum = 0
    odd_digit_sum = 0
    current_number_as_string = str(current_number)
    for index, digit in enumerate(current_number_as_string):
        if index % 2 == 0:
            odd_digit_sum += int(digit)
        else:
            even_digit_sum += int(digit)
    if even_digit_sum == odd_digit_sum:
        print(current_number_as_string, end=" ")

# 3

sum_of_prime_numbers = 0
sum_of_non_prime_numbers = 0
command = input()
while command != "stop":
    current_number = int(command)
    if current_number < 0:
        print("Number is negative.")
    else:
        current_number_is_prime = True
        for number in range(2, current_number):
            if current_number % number == 0:
                current_number_is_prime = False
                break
        if current_number_is_prime:  # if current_number_is_prime==True
            sum_of_prime_numbers += current_number
        else:
            sum_of_non_prime_numbers += current_number
    command = input()
print(f"Sum of all prime numbers is: {sum_of_prime_numbers}")
print(f"Sum of all non prime numbers is: {sum_of_non_prime_numbers}")

# 4

number_of_jury = int(input())
number_of_presentations = 0
final_average_grade = 0
command = input()
while command != "Finish":
    current_presentation_name = command
    number_of_presentations += 1
    current_presentation_grade = 0
    for presentation_grade in range(number_of_jury):
        current_grade = float(input())
        current_presentation_grade += current_grade
    current_presentation_grade /= number_of_jury  # current_presentation_grade = current_presentation_grade / number_of_jury
    print(f"{current_presentation_name} - {current_presentation_grade:.2f}.")
    final_average_grade += current_presentation_grade
    command = input()
final_average_grade /= number_of_presentations  # final_average_grade = final_average_grade / number_of_presentations
print(f"Student's final assessment is {final_average_grade:.2f}.")

# 5

number = int(input())
for current_number in range(1111, 9999 + 1):
    number_is_special = True
    current_number_as_string = str(current_number)
    for current_digit in current_number_as_string:
        if int(current_digit) == 0 or number % int(current_digit) != 0:
            number_is_special = False
            break
    if number_is_special:  # if number_is_special == True
        print(current_number_as_string, end=" ")

# 6

student_tickets_counter = 0
standard_tickets_counter = 0
kid_tickets_counter = 0
command = input()
while command != "Finish":
    movie_name = command
    free_places = int(input())
    sold_tickets = 0
    total_places_in_the_hall = free_places
    while free_places > 0:
        ticket_type = input()
        if ticket_type == "End":
            break
        elif ticket_type == "student":
            student_tickets_counter += 1
        elif ticket_type == "standard":
            standard_tickets_counter += 1
        elif ticket_type == "kid":  # else
            kid_tickets_counter += 1
        free_places -= 1
        sold_tickets += 1
    percent_full_hall = sold_tickets / total_places_in_the_hall * 100
    print(f"{movie_name} - {percent_full_hall:.2f}% full.")
    command = input()
total_tickets_counter = student_tickets_counter + standard_tickets_counter + kid_tickets_counter
students_percent = student_tickets_counter / total_tickets_counter * 100
standard_percent = standard_tickets_counter / total_tickets_counter * 100
kids_percent = kid_tickets_counter / total_tickets_counter * 100
print(f"Total tickets: {total_tickets_counter}")
print(f"{students_percent:.2f}% student tickets.")
print(f"{standard_percent:.2f}% standard tickets.")
print(f"{kids_percent:.2f}% kids tickets.")