# def concatenate(*args, **kwargs):
#     temp_string = ''
#     final_string = ''
#
#     for args_arguments in args:
#         if args_arguments in kwargs.keys():
#             new_argument = kwargs[args_arguments]
#             temp_string = temp_string.replace(temp_string, new_argument)
#             final_string += temp_string
#             temp_string = ''
#         else:
#             for letter in args_arguments:
#                 if letter in kwargs.keys():
#                     new_letter = kwargs[letter]
#                     letter = letter.replace(letter, new_letter)
#                     final_string += letter
#                     temp_string = ''
#                 else:
#                     final_string += letter
#                     temp_string = ''
#
#     return final_string


def concatenate(*args, **kwargs):
    final_string = ''.join(args)

    for key in kwargs:
        final_string = final_string.replace(key, kwargs[key])

    return final_string


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))