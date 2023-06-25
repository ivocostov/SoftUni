initial_text = input()

occurrences = {}

for letter in initial_text:
    if letter not in occurrences.keys():
        occurrences[letter] = 1
    else:
        occurrences[letter] += 1

for key, value in sorted(occurrences.items()):
    print(f"{key}: {value} time/s")