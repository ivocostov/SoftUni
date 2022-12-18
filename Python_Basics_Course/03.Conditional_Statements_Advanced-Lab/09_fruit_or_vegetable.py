fruit_or_vegie = input()

if fruit_or_vegie == 'banana' or fruit_or_vegie == 'apple' or fruit_or_vegie == 'kiwi' or fruit_or_vegie == 'cherry' or \
        fruit_or_vegie == 'lemon' or fruit_or_vegie == 'grapes':
    print('fruit')
elif fruit_or_vegie == 'tomato' or fruit_or_vegie == 'cucumber' or fruit_or_vegie == 'pepper' or \
        fruit_or_vegie == 'carrot':
    print('vegetable')
else:
    print('unknown')