user_input = input().split()

filtered_words = [word for word in user_input if len(word) % 2 == 0]
print('\n'.join(filtered_words))
