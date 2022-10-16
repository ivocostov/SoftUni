current_string = input()
double_letter_word = ""
while current_string != 'End':
    if current_string != 'SoftUni':
        for letter in current_string:
            double_letter_word += letter + letter
        print(double_letter_word)
    current_string = input()
    double_letter_word = ""



