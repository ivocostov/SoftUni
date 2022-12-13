string_of_banned_words = input().split(", ")
text = input()

for banned_word in string_of_banned_words:
    if banned_word in text:
        text = text.replace(banned_word, "*" * len(banned_word))

print(text)
