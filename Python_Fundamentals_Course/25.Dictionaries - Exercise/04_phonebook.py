phonebook = {}

while True:
    phonebook_entry = input()
    if "-" not in phonebook_entry:
        break

    person, phone_number = phonebook_entry.split("-")
    phonebook[person] = phone_number

searched_people = int(phonebook_entry)

for name in range(searched_people):
    searched_name = input()
    if searched_name not in phonebook.keys():
        print(f"Contact {searched_name} does not exist.")
    else:
        print(f"{searched_name} -> {phonebook[searched_name]}")
