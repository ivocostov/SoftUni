user_input = input().split(' ')
palindrom_example = input()

found_palindroms = []

for palindrom in user_input:
    if palindrom == ''.join(reversed(palindrom)):
        found_palindroms.append(palindrom)
print(found_palindroms)
print(f"Found palindrome {found_palindroms.count(palindrom_example)} times")
