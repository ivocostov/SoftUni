age_of_subject = float(input())
gender = input()

if age_of_subject >= 16 and gender == 'm':
    print('Mr.')
elif age_of_subject < 16 and gender == 'm':
    print('Master')
elif age_of_subject >= 16 and gender == "f":
    print('Ms.')
elif age_of_subject < 16 and gender == 'f':
    print('Miss')


