def add_phone(phones_list, phone):
    if phone not in phones_list:
        phones_list.append(phone)
    return phones_list


def remove_phone(phones_list, phone):
    if phone in phones_list:
        phones_list.remove(phone)
    return phones_list


def bonus_phone(phones_list, old_phone, new_phone):
    if old_phone in phones_list:
        old_phone_index = phones_list.index(old_phone)
        phones_list.insert(old_phone_index + 1, new_phone)
    return phones_list


def last_phone(phones_list, phone):
    if phone in phones_list:
        phones_list.remove(phone)
        phones_list.append(phone)
    return phones_list


def phone_shop(phones_list):
    while True:
        current_command = input()

        if current_command == "End":
            break

        command, phone = current_command.split(" - ")

        if command == "Add":
            phones_list = add_phone(phones_list, phone)
        elif command == "Remove":
            phones_list = remove_phone(phones_list, phone)
        elif command == "Bonus phone":
            old_phone, new_phone = phone.split(':')
            phones_list = bonus_phone(phones_list, old_phone, new_phone)
        elif command == "Last":
            phones_list = last_phone(phones_list, phone)

    print(', '.join(phones_list))


list_of_phones = input().split(', ')
phone_shop(list_of_phones)
