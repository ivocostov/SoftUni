user_string = input()

resulting_string = ""
temporary_letter = ""

for character in user_string:
    if character != temporary_letter:
        resulting_string += character
        temporary_letter = character

print(resulting_string)



"""
Write a program that reads a string from the console and replaces any sequence of the same letters with a single
corresponding letter.

EXAMPLES:

                                    Input:                              Output:
                            aaaaabbbbbcdddeeeedssaa                    abcdedsa
                            qqqwerqwecccwd                             qwerqwecwd
"""