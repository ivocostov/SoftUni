import re

count_of_inputs = int(input())
successful_registrations = 0

for num in range(count_of_inputs):
    user_input = input()

    pattern = r'(U\$)([A-Z][a-z]{2,})\1(P\@\$)([A-Za-z]{5,}[\d]+)\3'
    result = re.findall(pattern, user_input)

    if result:
        print("Registration was successful")
        print(f"Username: {result[0][1]}, Password: {result[0][-1]}")
        successful_registrations += 1
    else:
        print("Invalid username or password")

print(f"Successful registrations: {successful_registrations}")
