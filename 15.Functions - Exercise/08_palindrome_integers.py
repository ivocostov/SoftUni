def palindrome_integers(number):
    for current_number in number:
        if current_number == current_number[:: -1]:
            print(True)
        else:
            print(False)


user_input = input().split(', ')
palindrome_integers(user_input)
