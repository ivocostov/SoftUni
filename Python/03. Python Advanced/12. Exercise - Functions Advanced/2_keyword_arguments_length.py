def kwargs_length(**kwargs):
    lenght_of_dictionary = len(kwargs)
    return lenght_of_dictionary


# dictionary = {'name': 'Peter', 'age': 25}
# print(kwargs_length(**dictionary))

dictionary = {}
print(kwargs_length(**dictionary))
