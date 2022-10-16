# 1.	No Vowels

text = input()
vowels = ['a', 'o', 'u', 'e', 'i']
result = ''
for ch in text:
    if ch.lower() not in vowels:
        result += ch

print(result)

# 2.	Trains
number = int(input())
wagons = [0] * number
command = input()

while True:
    command = input()

    if command == 'End':
        break

    split_command = command.split(' ')  # insert 0 15
    current_command = split_command[0]

    if current_command == 'add':
        people_to_add = int(split_command[1])
        wagons[-1] += people_to_add

    elif current_command == 'insert':
        index = int(split_command[1])  # insert 0 15
        number_of_people = int(split_command[2])
        wagons[index] += number_of_people

    elif current_command == 'leave':
        index = int(split_command[1])
        people_to_leave = int(split_command[2])
        wagons[index] -= people_to_leave

print(wagons)

# 3.	To-do List
tasks = []

while True:
    command = input()

    if command == 'End':
        break

    split_command = command.split('-')
    priority = int(split_command[0])
    current_task = split_command[1]

    tasks.append([priority, current_task])

sorted_tasks = []
for task_data in sorted(tasks):
    sorted_tasks.append(task_data[1])

print(sorted_tasks)


# 4.	Palindrome Strings
def palindrome_filtered(word):
    if word == word[::-1]:
        return word


words = input().split(' ')
palindrome = input()

palindrome_list = [word for word in words if palindrome_filtered(word)]
palindrome_counter = palindrome_list.count(palindrome)

print(palindrome_list)
print(f'Found palindrome {palindrome_counter} times')

# 5.	Sorting Names
names = input().split(', ')
result = sorted(names, key=lambda item: (-len(item), item))
print(result)

# 6.	Even Numbers
numbers = list(map(int, input().split(', ')))
indices = [num for num in range(len(numbers)) if numbers[num] % 2 == 0]
print(indices)

# speed timeit
import timeit

a = timeit.timeit(stmt='''lst = []
for n in range(10000):
    lst.append(n)''', number=10000)

b = timeit.timeit(stmt='lst = [n for n in range(10000)]', number=10000)

print(a)
print(b)