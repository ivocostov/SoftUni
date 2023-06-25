<<<<<<< HEAD
def username_length(name):
    if 3 <= len(name) <= 16:
        return True
    return False


def characters_validity(name):
    for character in name:
        if not (character.isalnum() or character == "-" or character == "_"):
            return False
    return True


def no_redundant_symbols(name):
    if " " in name:
        return False
    return True


def valid_usernames(name):
    if username_length(name) and characters_validity(name) and no_redundant_symbols(name):
        return True
    return False


username_input = input().split(", ")
for username in username_input:
    if valid_usernames(username):
        print(username)





"""
Write a program that reads usernames on a single line (separated by ", ") and prints all valid usernames on separate lines.
 A valid username:
    •	has length between 3 and 16 characters inclusive
    •	can contain only letters, numbers, hyphens, and underscores
    •	has no redundant symbols before, after, or in between

EXAMPLES:
                            Input:                                              Output:
        sh, too_long_username, !lleg@l ch@rs, jeffbutt    |                     jeffbutt
        Jeff, john45, ab, cd, peter-ivanov, @smith        |                     Jeff
                                                          |                     John45
                                                          |                     peter-ivanov
=======
def username_length(name):
    if 3 <= len(name) <= 16:
        return True
    return False


def characters_validity(name):
    for character in name:
        if not (character.isalnum() or character == "-" or character == "_"):
            return False
    return True


def no_redundant_symbols(name):
    if " " in name:
        return False
    return True


def valid_usernames(name):
    if username_length(name) and characters_validity(name) and no_redundant_symbols(name):
        return True
    return False


username_input = input().split(", ")
for username in username_input:
    if valid_usernames(username):
        print(username)





"""
Write a program that reads usernames on a single line (separated by ", ") and prints all valid usernames on separate lines.
 A valid username:
    •	has length between 3 and 16 characters inclusive
    •	can contain only letters, numbers, hyphens, and underscores
    •	has no redundant symbols before, after, or in between

EXAMPLES:
                            Input:                                              Output:
        sh, too_long_username, !lleg@l ch@rs, jeffbutt    |                     jeffbutt
        Jeff, john45, ab, cd, peter-ivanov, @smith        |                     Jeff
                                                          |                     John45
                                                          |                     peter-ivanov
>>>>>>> 36496de6931529b811d0c463d6ad38e232c5703a
"""