day_of_the_week = input()
price = 0

if day_of_the_week == 'Monday':
    price = 12
elif day_of_the_week == 'Tuesday':
    price = 12
elif day_of_the_week == 'Wednesday':
    price = 14
elif day_of_the_week == 'Thursday':
    price = 14
elif day_of_the_week == 'Friday':
    price = 12
elif day_of_the_week == 'Saturday':
    price = 16
elif day_of_the_week == 'Sunday':
    price = 16

print(price)
