def character_multiplier(string_1, string_2):
    total_sum = 0

    if len(string_1) > len(string_2):
        for index in range(len(string_2)):
            total_sum += ord(string_1[index]) * ord(string_2[index])
        for index in range(len(string_2), len(string_1)):
            total_sum += ord(string_1[index])
        return total_sum
    elif len(string_2) > len(string_1):
        for index in range(len(string_1)):
            total_sum += ord(string_2[index]) * ord(string_1[index])
        for index in range(len(string_1), len(string_2)):
            total_sum += ord(string_2[index])
        return total_sum
    else:
        for index in range(len(first_string)):
            total_sum += ord(string_1[index]) * ord(string_2[index])
        return total_sum


first_string, second_string = input().split()
print(character_multiplier(first_string, second_string))

"""
Create a program that receives two strings on a single line separated by a single space.
Then, it prints the sum of their multiplied character codes as follows: multiply str1[0] with str2[0] and add the result
to the total sum, then continue with the next two characters. If one of the strings is longer than the other,
add the remaining character codes to the total sum without multiplication.

EXAMPLES:
                        Input:                |                      Output:
                    George Peter              |                       52114
                    123 522	                  |                       7647
                    a aaaa                    |                       9700
"""
