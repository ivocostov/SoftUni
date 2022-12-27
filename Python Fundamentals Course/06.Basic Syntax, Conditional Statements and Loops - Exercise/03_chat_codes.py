count_of_messages = int(input())

for current_msg_count in range(count_of_messages):
    number_in_msg = int(input())
    if number_in_msg == 88:
        print("Hello")
    elif number_in_msg == 86:
        print("How are you?")
    elif number_in_msg < 88:
        print("GREAT!")
    elif number_in_msg > 88:
        print("Bye.")
