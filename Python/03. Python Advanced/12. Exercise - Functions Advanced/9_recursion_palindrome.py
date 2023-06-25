def palindrome(word, index, last_index=-1):
    if index == len(word) // 2:                 # това е дъното на рекурсията, т.е. е останала само една буква
        return f"{word} is a palindrome"

    if word[index] != word[last_index]:         # това е другото дъно на рекурсията, т.е първата сравнявана буква е различна от втората сравнявана буква
        return f"{word} is not a palindrome"

    return palindrome(word, index + 1, last_index - 1)


#print(palindrome("abcba", 0))

print(palindrome("peter", 0))
