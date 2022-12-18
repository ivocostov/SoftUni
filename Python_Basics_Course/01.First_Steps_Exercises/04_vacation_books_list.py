from math import floor

number_of_book_pages = int(input())
pages_read_in_an_hour = int(input())
days_needed_the_book_to_be_read = int(input())

total_hours_needed_for_the_book_to_be_read = number_of_book_pages / pages_read_in_an_hour
total_days_needed_the_book_to_be_read = total_hours_needed_for_the_book_to_be_read / days_needed_the_book_to_be_read
print(floor(total_days_needed_the_book_to_be_read))
# или print(int(total_days_needed_the_book_to_be_read)), без да се импортва библиотека
