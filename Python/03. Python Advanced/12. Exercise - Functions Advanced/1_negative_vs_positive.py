numbers = [int(x) for x in input().split()]

sum_of_positive_numbers = 0
sum_of_negative_numbers = 0

for num in numbers:
    if num < 0:
        sum_of_negative_numbers += num
    else:
        sum_of_positive_numbers += num

print(f'{sum_of_negative_numbers}\n'
      f'{sum_of_positive_numbers}')

if sum_of_positive_numbers > abs(sum_of_negative_numbers):
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")
