<<<<<<< HEAD
synonyms = {}

command = input()

for _ in range(int(command)):
    word = input()
    synonym = input()
    if word not in synonyms.keys():
        synonyms[word] = []
    synonyms[word].append(synonym)

for current_word, current_synonym in synonyms.items():
    print(f"{current_word} - {', '.join(current_synonym)}")
=======
synonyms = {}

command = input()

for _ in range(int(command)):
    word = input()
    synonym = input()
    if word not in synonyms.keys():
        synonyms[word] = []
    synonyms[word].append(synonym)

for current_word, current_synonym in synonyms.items():
    print(f"{current_word} - {', '.join(current_synonym)}")
>>>>>>> 36496de6931529b811d0c463d6ad38e232c5703a
