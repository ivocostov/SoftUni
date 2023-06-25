number = int(input())

positive_numbers_list = []
negative_numbers_list = []
count_positives = 0
sum_of_negatives = 0

for current_num in range(number):
    current_number = int(input())
    if current_number >= 0:
        positive_numbers_list.append(current_number)
        count_positives += 1
    else:
        negative_numbers_list.append(current_number)
        sum_of_negatives += current_number

print(positive_numbers_list)
print(negative_numbers_list)
#print(f"Count of positives: {count_positives}")
#print(f"Sum of negatives: {sum_of_negatives}")
print(f"Count of positives: {len(positive_numbers_list)} \n"
      f"Sum of negatives: {sum(negative_numbers_list)}")
