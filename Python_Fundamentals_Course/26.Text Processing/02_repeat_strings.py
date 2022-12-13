user_input = input().split()

for word in user_input:
    print(word * len(word), end="")