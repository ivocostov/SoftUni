factor = int(input())
count = int(input())

resulted_numbers_list = []

for current_number in range(1, count + 1):
    resulted_numbers_list.append(current_number * factor)

print(resulted_numbers_list)
