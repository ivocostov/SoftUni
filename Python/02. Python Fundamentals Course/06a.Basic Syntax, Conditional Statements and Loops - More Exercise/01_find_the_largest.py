# number = input()
# list = [*number]
# largest_number = ""
#
# list.sort(reverse=True)
#
# largest_number = largest_number.join(list)
#
#print(largest_number)

number = input() # взимам инпута като string
sorted_string = sorted(number) # сортирам го по азбучен ред
sorted_number = sorted_string[::-1] # Обръщам го
conversion = (str(integer) for integer in sorted_number) # това го взех от нета
list_to_integer = "".join(conversion) # това също го взех от нета
max_number = int(list_to_integer) # тук вече знам, че го каствам към инт
print(max_number) # работи