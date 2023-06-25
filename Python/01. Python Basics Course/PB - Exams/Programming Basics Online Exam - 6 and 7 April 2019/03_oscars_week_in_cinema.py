movie_name = input()
type_of_hall = input()
tickets_sold = int(input())

total_tickets_price = 0

if movie_name == 'A Star Is Born':
    if type_of_hall == 'normal':
        total_tickets_price = tickets_sold * 7.5
    elif type_of_hall == 'luxury':
        total_tickets_price = tickets_sold * 10.5
    elif type_of_hall == 'ultra luxury':
        total_tickets_price = tickets_sold * 13.5
if movie_name == 'Bohemian Rhapsody':
    if type_of_hall == 'normal':
        total_tickets_price = tickets_sold * 7.35
    elif type_of_hall == 'luxury':
        total_tickets_price = tickets_sold * 9.45
    elif type_of_hall == 'ultra luxury':
        total_tickets_price = tickets_sold * 12.75
if movie_name == 'Green Book':
    if type_of_hall == 'normal':
        total_tickets_price = tickets_sold * 8.15
    elif type_of_hall == 'luxury':
        total_tickets_price = tickets_sold * 10.25
    elif type_of_hall == 'ultra luxury':
        total_tickets_price = tickets_sold * 13.25
if movie_name == 'The Favourite':
    if type_of_hall == 'normal':
        total_tickets_price = tickets_sold * 8.75
    elif type_of_hall == 'luxury':
        total_tickets_price = tickets_sold * 11.55
    elif type_of_hall == 'ultra luxury':
        total_tickets_price = tickets_sold * 13.95

print(f"{movie_name} -> {total_tickets_price:.2f} lv.")

