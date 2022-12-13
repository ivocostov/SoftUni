user_input = input().split(" ")

#bakery_dict = {}

# решение с  for loop
# for index in range(0, len(user_input), 2): # обхожда речника със стъпка 2 за да може да взима по два елемента. Примерно индекс 0 и 1, след това 2 и 3 и т.н
    #bakery_dict[user_input[index]] = int(user_input[index + 1]) #Взима първия елемент и го прави ключ а втория го прави стойност към този ключ

# решение с dictionary comprehension ( трябва да се закоментира и bakery_dict = {} )
bakery_dict = {user_input[index]: int(user_input[index + 1]) for index in range(0, len(user_input), 2)}

print(bakery_dict)



# #########################################################################################################################
#                                                                                                                         #
#  bakery_dict[user_input[index]] = int(user_input[index + 1]) Е СЪЩОТО КАТО user_input[index]: int(user_input[index + 1] #
#                                                                                                                         #
# #########################################################################################################################