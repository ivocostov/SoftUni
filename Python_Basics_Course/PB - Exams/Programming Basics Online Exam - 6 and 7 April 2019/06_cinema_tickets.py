student_tickets_sold_counter = 0
standard_tickets_sold_counter = 0
kids_tickets_sold_counter = 0
total_tickets_sold = 0

command = input()

while command != 'Finish':

    movie_name = command
    saloon_free_places = int(input())
    sold_tickets_per_projection = 0
    free_places_left = saloon_free_places

    while free_places_left > 0:
        type_of_ticket = input()
        if type_of_ticket == 'End':
            break
        if type_of_ticket == 'student':
            student_tickets_sold_counter += 1

        elif type_of_ticket == 'standard':
            standard_tickets_sold_counter += 1

        elif type_of_ticket == 'kid':
            kids_tickets_sold_counter += 1

        free_places_left -= 1
        sold_tickets_per_projection += 1
        total_tickets_sold += 1

    print(f"{movie_name} - {sold_tickets_per_projection / saloon_free_places * 100:.2f}% full.")
    command = input()

print(f"Total tickets: {total_tickets_sold}")
print(f"{student_tickets_sold_counter / total_tickets_sold * 100:.2f}% student tickets.")
print(f"{standard_tickets_sold_counter / total_tickets_sold * 100:.2f}% standard tickets.")
print(f"{kids_tickets_sold_counter / total_tickets_sold * 100:.2f}% kids tickets.")

