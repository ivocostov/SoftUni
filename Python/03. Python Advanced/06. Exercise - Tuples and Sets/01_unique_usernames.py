number_of_usernames = int(input())

username_list = set()

for name in range(number_of_usernames):
    username = input()
    username_list.add(username)
print(*username_list, sep='\n')
