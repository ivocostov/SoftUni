#### WORKED AFTER THE EXAM IS FINISHED ####


def like(guest, meal):
    if guest not in guests_dict['guests_list']:
        guests_dict['guests_list'][guest] = [meal]
    else:
        if meal not in guests_dict['guests_list'][guest]:
            guests_dict['guests_list'][guest].append(meal)


def dislike(guest, meal):
    if guest in guests_dict['guests_list']:
        if meal in guests_dict['guests_list'][guest]:
            guests_dict['guests_list'][guest].remove(meal)
            print(f"{guest} doesn't like the {meal}.")
            guests_dict['counter'].append(1)

        else:
            print(f"{guest} doesn't have the {meal} in his/her collection.")
    else:
        print(f"{guest} is not at the party.")


guests_dict = {'guests_list': {}, 'counter': []}

while True:
    command = input()
    if command == 'Stop':
        break

    current_command = command.split('-')

    action = current_command[0]
    if action == 'Like':
        guest = current_command[1]
        meal = current_command[2]
        like(guest, meal)
    elif action == 'Dislike':
        guest = current_command[1]
        meal = current_command[2]
        dislike(guest, meal)

final_guest_list = guests_dict['guests_list']
counter = sum(guests_dict['counter'])

for guest, meals in final_guest_list.items():
    dishes = ', '.join(meals)
    print(f"{guest}: {dishes}")
print(f"Unliked meals: {counter}")


######################################################################################################################

# WORKING SOLUTION

# guests_dict = {}
# unliked_meals = 0
#
# while True:
#
#     command = input()
#     if command == 'Stop':
#         break
#
#     current_command = command.split('-')
#
#     action = current_command[0]
#     if action == 'Like':
#         guest = current_command[1]
#         meal = current_command[2]
#         if guest not in guests_dict.keys():
#             guests_dict[guest] = [meal]
#         else:
#             if meal not in guests_dict.keys():
#                 guests_dict[guest].append(meal)
#
#     elif action == 'Dislike':
#         guest = current_command[1]
#         meal = current_command[2]
#
#         if guest in guests_dict.keys():
#             if meal in guests_dict[guest]:
#                 guests_dict[guest].remove(meal)
#                 print(f"{guest} doesn't like the {meal}.")
#                 unliked_meals += 1
#
#             else:
#                 print(f"{guest} doesn't have the {meal} in his/her collection.")
#         else:
#             print(f"{guest} is not at the party.")
#
#
# for guest, meals in guests_dict.items():
#     dishes = ', '.join(meals)
#     print(f"{guest}: {dishes}")
# print(f"Unliked meals: {unliked_meals}")


########################################################################################################################
#
# 3rd PARTY SOLUTION
#
# liked_meals = {}
# unliked_meals = 0
#
#
# def liked_meal(guest, meal):
#     liked_meals[guest] = liked_meals.get(guest, [])
#     if meal not in liked_meals[guest]:
#         liked_meals[guest].append(meal)
#
#
# def disliked_meal(guest, meal):
#     global unliked_meals
#     if guest not in liked_meals:
#         print(f"{guest} is not at the party.")
#     elif meal not in liked_meals[guest]:
#         print(f"{guest} doesn't have the {meal} in his/her collection.")
#     elif meal in liked_meals[guest]:
#         liked_meals[guest].remove(meal)
#         unliked_meals += 1
#         print(f"{guest} doesn't like the {meal}.")
#
#
# def show_result():
#     if liked_meals:
#         for guest in liked_meals:
#             print(f"{guest}: {', '.join(liked_meals[guest])}")
#     print(f"Unliked meals: {unliked_meals}")
#
#
# command_func = {
#     "Like": liked_meal,
#     "Dislike": disliked_meal
# }
#
# command = input()
#
# while command != "Stop":
#     command_type, guest, meal = command.split("-")
#     command_func[command_type](guest, meal)
#     command = input()
#
# show_result()
#
########################################################################################################################