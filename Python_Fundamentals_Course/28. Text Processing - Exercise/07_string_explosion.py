user_string = input()
new_string = ""
power_counter = 0

for index in range(len(user_string)):
    if power_counter > 0 and user_string[index] != ">":
        power_counter -= 1
    elif user_string[index] == ">":
        power_counter += int(user_string[index + 1])
        new_string += user_string[index]
    else:
        new_string += user_string[index]

print(new_string)







"""
Write a program that reads a string from the console that contains:
    •	Explosions marked with '>'
    •	Immediately after the mark, there will be an integer x, which signifies the strength of the explosion
    •	Any other characters
Your task is to delete x characters, starting after the exploded character ('>'). If you find another explosion mark ('>') while deleting characters, you should add the strength to your previous explosion. You should not delete the explosion character – '>'.
When all characters are processed, print the final string.

CONSTRAINTS:

    •	You will always receive strength for the explosions
    •	The path will consist only of letters from the Latin alphabet, integers, and the char '>'
    •	The strength of the punches will be in the interval [0…9]

EXAMPLES:
                Input:                            Output:                               Comments:
            abv>1>1>2>2asdasd                   abv>>>>dasd                    1st explosion is at index 3, with a
    pesho>2sis>1a>2akarate>4hexmaster        pesho>is>a>karate>master          after the explosion character. The string
                                                                               will look like this: abv>>1>2>2asdasd
                                                                               2nd explosion is with strength one, and
                                                                               the string transforms to this:
                                                                               abv>>>2>2asdasd
                                                                               3rd explosion is now with a strength
                                                                               of 2. We delete the digit, and we find
                                                                               another explosion. At this point,
                                                                               the string looks like this:
                                                                               abv>>>>2asdasd. 4th explosion is with
                                                                               strength 2. We have 1 strength left from
                                                                               the previous explosion, and we add the
                                                                               strength of the current explosion to what
                                                                               is left, which adds up to a total strength
                                                                               of 3. We delete the next three characters,
                                                                               and we receive the string abv>>>>dasd
                                                                               We do not have any more explosions,
                                                                               and we print the result: abv>>>>dasd
"""