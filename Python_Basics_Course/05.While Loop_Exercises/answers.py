https://pastebin.com/Ep9WfnUC

# 1

searched_book = input()
books_counter = 0
book_is_found = False
current_book = input()
while current_book != "No More Books":
    if current_book == searched_book:
        book_is_found = True
        break
    books_counter += 1
    current_book = input()
if book_is_found:  # if book_is_found == True
    print(f"You checked {books_counter} books and found it.")
else:  # book_is_found == False
    print("The book you search is not here!")
    print(f"You checked {books_counter} books.")

# 2

maximum_bad_grades = int(input())
average_grade = 0
total_problems_solved = 0
last_problem = ''
bad_grades_counter = 0
is_expelled = False
current_problem = input()
while current_problem != "Enough":
    current_grade = int(input())
    if current_grade <= 4:  # Bad grade
        bad_grades_counter += 1
        if bad_grades_counter == maximum_bad_grades:
            is_expelled = True
            break
    average_grade += current_grade
    total_problems_solved += 1
    last_problem = current_problem
    current_problem = input()
if is_expelled:  # if is_expelled == True ; if bad_grades_counter == maximum_bad_grades
    print(f"You need a break, {bad_grades_counter} poor grades.")
else:  # current_problem == "Enough"
    average_grade /= total_problems_solved  # average_grade = average_grade / total_problems_solved
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {total_problems_solved}")
    print(f"Last problem: {last_problem}")

# 3

needed_money = float(input())
money_in_hand = float(input())
spending_counter = 0
total_days_counter = 0
spending_too_many_days = False
while money_in_hand < needed_money:
    action = input()
    current_sum = float(input())
    total_days_counter += 1
    if action == "spend":
        spending_counter += 1
        if spending_counter == 5:
            spending_too_many_days = True
            break
        money_in_hand -= current_sum
        if money_in_hand < 0:
            money_in_hand = 0
    else:  # action =="save"
        money_in_hand += current_sum
        spending_counter = 0
if spending_too_many_days:  # if spending_too_many_days == True:
    print("You can't save the money.")
    print(f"{total_days_counter}")
else:
    print(f"You saved the money for {total_days_counter} days.")

# 4

target_steps = 10000
total_steps = 0
while total_steps < target_steps:  # total_steps < 10000
    command = input()
    if command == "Going home":
        last_steps = int(input())
        total_steps += last_steps
        break
    current_steps = int(command)
    total_steps += current_steps
difference = abs(total_steps - target_steps)
if total_steps >= target_steps:
    print("Goal reached! Good job!")
    print(f"{difference} steps over the goal!")
else:
    print(f"{difference} more steps to reach goal.")

# 5


change = float(input())
change = int(change * 100)
coins_counter = 0
coins_counter += change // 200
change = change % 200
coins_counter += change // 100
change = change % 100
coins_counter += change // 50
change = change % 50
coins_counter += change // 20
change = change % 20
coins_counter += change // 10
change = change % 10
coins_counter += change // 5
change = change % 5
coins_counter += change // 2
change = change % 2
coins_counter += change // 1
change = change % 1
print(coins_counter)

# 5.1

change = float(input())
change = int(change * 100)
coins_counter = 0
while change > 0:
    if change - 200 >= 0:
        coins_counter += 1
        change -= 200
    elif change - 100 >= 0:
        coins_counter += 1
        change -= 100
    elif change - 50 >= 0:
        coins_counter += 1
        change -= 50
    elif change - 20 >= 0:
        coins_counter += 1
        change -= 20
    elif change - 10 >= 0:
        coins_counter += 1
        change -= 10
    elif change - 5 >= 0:
        coins_counter += 1
        change -= 5
    elif change - 2 >= 0:
        coins_counter += 1
        change -= 2
    elif change - 1 == 0:
        coins_counter += 1
        change -= 1
print(coins_counter)

# 6

width = int(input())
length = int(input())
cake_is_over = False
total_pieces = width * length
command = input()
while command != "STOP":
    current_pieces = int(command)
    total_pieces -= current_pieces
    if total_pieces < 0:
        cake_is_over = True
        break
    command = input()
if cake_is_over:
    print(f"No more cake left! You need {abs(total_pieces)} pieces more.")
else:
    print(f"{total_pieces} pieces are left.")

# 7

width = int(input())
length = int(input())
height = int(input())
there_is_more_free_space = True
total_volume = width * length * height
command = input()
while command != "Done":
    current_number_of_boxes = int(command)
    total_volume -= current_number_of_boxes
    if total_volume < 0:
        there_is_more_free_space = False
        break
    command = input()
if there_is_more_free_space:  # if total_volume >= 0
    print(f"{total_volume} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(total_volume)} Cubic meters more.")