<<<<<<< HEAD
"""
ПРИНТИРАНЕ ПО КРИТЕРИЙ С ДВЕ СРАВНЯВАНИЯ

You know the judge system, right?! Your job is to create a program similar to the Judge system.
You will receive several input lines in one of the following formats:
"{username} -> {contest} -> {points}"
"""

'''
The "contest" and "username" are strings, the given "points" will be an integer number. You need to keep track of every 
contest and points of each user: 

•	If the user has already participated in the contest, update their points only if the new ones are more than the 
    older ones.
•	Otherwise, just save the data - contest, username, and points.

Also, you need to keep individual statistics for each user - his/her final total points for all contests.
You should end your program when you receive the command "no more time". At that point, you should print each contest 
in order of input, for each contest print the participants ordered by points in descending order, then ordered by name 
in ascending order. After that, you should print individual statistics for every participant ordered by total points 
in descending order, and then by alphabetical order.
'''


def main_function(initial_data):
    while initial_data != 'no more time':
        username, contest, points = [int(x) if x.isdigit() else x for x in initial_data.split(' -> ')]
        if username not in users_dictionary.keys():
            users_dictionary[username] = {contest: points}

        if contest not in users_dictionary[username]:
            users_dictionary[username][contest] = points

        if contest in users_dictionary[username].keys():
            if int(users_dictionary[username].get(contest)) < points:
                users_dictionary[username][contest] = points

        if contest not in contest_dictionary.keys():
            contest_dictionary[contest] = {username: points}
        else:
            contest_dictionary[contest][username] = points
        initial_data = input()


def show_results():
    global row_number

    for course in contest_dictionary.keys():
        print(f"{course}: {len(contest_dictionary[course])} participants")
        row_number = 1
        for current_user, users_points in sorted(contest_dictionary[course].items(), key=lambda x: (-x[1], x[0])):
            print(f"{row_number}. {current_user} <::> {users_points}")
            row_number += 1
        continue

    print("Individual standings:")
    row_number = 1
    total_points = {users: sum(users_dictionary[users].values()) for users in users_dictionary}
    for individual, value in sorted(total_points.items(), key=lambda x: (-x[1], x[0])):
        print(f"{row_number}. {individual} -> {value}")
        row_number += 1


row_number = 1
users_dictionary, contest_dictionary = {}, {}
user_input = input()
main_function(user_input)
show_results()
=======
"""
ПРИНТИРАНЕ ПО КРИТЕРИЙ С ДВЕ СРАВНЯВАНИЯ

You know the judge system, right?! Your job is to create a program similar to the Judge system.
You will receive several input lines in one of the following formats:
"{username} -> {contest} -> {points}"
"""

'''
The "contest" and "username" are strings, the given "points" will be an integer number. You need to keep track of every 
contest and points of each user: 

•	If the user has already participated in the contest, update their points only if the new ones are more than the 
    older ones.
•	Otherwise, just save the data - contest, username, and points.

Also, you need to keep individual statistics for each user - his/her final total points for all contests.
You should end your program when you receive the command "no more time". At that point, you should print each contest 
in order of input, for each contest print the participants ordered by points in descending order, then ordered by name 
in ascending order. After that, you should print individual statistics for every participant ordered by total points 
in descending order, and then by alphabetical order.
'''


def main_function(initial_data):
    while initial_data != 'no more time':
        username, contest, points = [int(x) if x.isdigit() else x for x in initial_data.split(' -> ')]
        if username not in users_dictionary.keys():
            users_dictionary[username] = {contest: points}

        if contest not in users_dictionary[username]:
            users_dictionary[username][contest] = points

        if contest in users_dictionary[username].keys():
            if int(users_dictionary[username].get(contest)) < points:
                users_dictionary[username][contest] = points

        if contest not in contest_dictionary.keys():
            contest_dictionary[contest] = {username: points}
        else:
            contest_dictionary[contest][username] = points
        initial_data = input()


def show_results():
    global row_number

    for course in contest_dictionary.keys():
        print(f"{course}: {len(contest_dictionary[course])} participants")
        row_number = 1
        for current_user, users_points in sorted(contest_dictionary[course].items(), key=lambda x: (-x[1], x[0])):
            print(f"{row_number}. {current_user} <::> {users_points}")
            row_number += 1
        continue

    print("Individual standings:")
    row_number = 1
    total_points = {users: sum(users_dictionary[users].values()) for users in users_dictionary}
    for individual, value in sorted(total_points.items(), key=lambda x: (-x[1], x[0])):
        print(f"{row_number}. {individual} -> {value}")
        row_number += 1


row_number = 1
users_dictionary, contest_dictionary = {}, {}
user_input = input()
main_function(user_input)
show_results()
>>>>>>> 36496de6931529b811d0c463d6ad38e232c5703a
