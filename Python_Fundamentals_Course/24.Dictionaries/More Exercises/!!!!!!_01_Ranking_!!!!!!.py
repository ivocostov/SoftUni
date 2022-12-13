"""
Here comes the final and the most interesting part – the Final ranking of the candidate-interns. The final ranking is
determined by the points of the interview tasks and by the points from the exams in SoftUni. Here is your final task.
You will receive some lines of input in the format "{contest}:{password for contest}" until you receive
"end of contests". Save that data because you will need it later. After that you will receive other type of inputs
in format "{contest}=>{password}=>{username}=>{points}" until you receive "end of submissions".
"""


def initial_dictionary(initial_data):
    while initial_data != 'end of contests':
        contest, password_for_contest = initial_data.split(':')
        contest_dictionary[contest] = password_for_contest
        initial_data = input()


'''
Check if the contest is valid (It is considered valid if you received it in the first type of input)
Check if the password is correct for the given contest
'''


def validation_check(contests, password, username, points):
    if contests in contest_dictionary.keys():
        if contest_dictionary.get(contests) == password:
            add_users(contests, username, points)


'''
If the contest and the password is valid, save the user with the contest they take part in (a user can take part in 
many contests) and the points the user has in the given contest. If you receive the same contest and the same user 
update the points only if the new ones are more than the older ones.
'''


def add_users(contest, username, points):
    if username not in users_dictionary.keys():
        users_dictionary[username] = {contest: points}
    elif contest not in users_dictionary[username].keys():
        users_dictionary[username][contest] = points
    elif username in users_dictionary.keys() and users_dictionary[username][contest] < points:
        users_dictionary[username][contest] = points


def main_function(users_dict):
    while True:
        current_command = input()
        if current_command == 'end of submissions':
            break

        contest, password, username, points = [int(x) if x.isdigit() else x for x in current_command.split("=>")]
        validation_check(contest, password, username, points)



def show_result():
    candidates = {name: sum(users_dictionary[name].values()) for name in users_dictionary}
    best_candidate = max(candidates, key=candidates.get)
    print(f"Best candidate is {best_candidate} with total {candidates[best_candidate]} points."
          f"\nRanking:")

    for name in sorted(users_dictionary):
        print(name)
        for contest, points in sorted(users_dictionary[name].items(), key=lambda item: -item[1]):
            print(f"#  {contest} -> {points}")


contest_dictionary = {}
users_dictionary = {}

initial_info = input()
initial_dictionary(initial_info)
main_function(users_dictionary)

show_result()