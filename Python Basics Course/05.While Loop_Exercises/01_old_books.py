book_label = input()
book_counter = 0
book_found = False
current_input = input()

while current_input != 'No More Books':
    if current_input == book_label:
        book_found = True
        break
    book_counter += 1
    current_input = input()
if book_found:
    print(f"You checked {book_counter} books and found it.")

if not book_found:
    print(f"The book you search is not here!")
    print(f"You checked {book_counter} books.")

