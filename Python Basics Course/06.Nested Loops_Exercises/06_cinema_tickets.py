student_tickets_counter = 0
standard_tickets_counter = 0
kids_tickets_counter = 0
total_tickets_sold = 0

command = input()

while command != "Finish":

    movie_name = command
    free_saloon_places = int(input())
    sold_tickets = 0
    saloon_places_left = free_saloon_places

    while free_saloon_places > 0:
        ticket_type = input()
        if ticket_type == "End":
            break
        elif ticket_type == "student":
            student_tickets_counter += 1
        elif ticket_type == "standard":
            standard_tickets_counter += 1
        elif ticket_type == "kids":
            kids_tickets_counter += 1
        total_tickets_sold += 1
        free_saloon_places -= 1
        sold_tickets += 1
    full_hall_percentage = sold_tickets / total_tickets_sold * 100
    print(f"{movie_name} - {full_hall_percentage:.2f}% full.")

    command = input()
students_percentage = student_tickets_counter / total_tickets_sold * 100
standard_percentage =  standard_tickets_counter / total_tickets_sold * 100
kids_percentage = kids_tickets_counter / total_tickets_sold * 100
print(f"Total tickets: {total_tickets_sold}")
print(f"{students_percentage:.2f}% student tickets")
print(f"{standard_percentage:.2f}% standard tickets")
print(f"{kids_percentage:.2f}% kids tickets")
