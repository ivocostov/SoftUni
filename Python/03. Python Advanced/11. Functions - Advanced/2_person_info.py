def get_info(name, age, town):
    return f"This is {name} from {town} and he is {age} years old"  # printing the values that corresponds to keys


print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))  # the keys are given to the function