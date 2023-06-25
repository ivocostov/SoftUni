number_of_guests = int(input())

guest_codes_list = set()

while True:
    name = input()
    if name == 'END':
        break
    elif name not in guest_codes_list:
        guest_codes_list.add(name)
    else:
        guest_codes_list.discard(name)

print(len(guest_codes_list))
print('\n'.join(sorted(guest_codes_list)))
