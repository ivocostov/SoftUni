user_text = input()

for index in range(len(user_text)):
    if user_text[index] == ":":
        print(user_text[index]+user_text[index + 1])

"""
Find all emoticons in the text. An emoticon always starts with ":" and is followed by a symbol.
The input will be provided as a single string.

EXAMPLES:
                                Input:                                              Output:
                There are so many emoticons nowadays :P.                            :P
                I have many ideas :O what input to place here :)                    :O
                                                                                    :)
"""