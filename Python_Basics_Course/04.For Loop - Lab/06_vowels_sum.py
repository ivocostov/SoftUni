word = input()
points = 0

for letter in range(0, len(word)):
    if word[letter] == "a":
        points += 1
    elif word[letter] == "e":
        points += 2
    elif word[letter] == "i":
        points += 3
    elif word[letter] == "o":
        points += 4
    elif word[letter] == "u":
        points += 5
print(points)



