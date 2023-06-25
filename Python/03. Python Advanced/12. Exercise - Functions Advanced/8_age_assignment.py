def age_assignment(*args, **kwargs):
    person_s_list = []

    for letter, age in kwargs.items():
        name = ''
        for current_name in args:
            if current_name.startswith(letter):
                name = current_name
                break

        person_s_list.append(f"{name} is {age} years old.")

    return '\n'.join(sorted(person_s_list))


#print(age_assignment("Peter", "George", G=26, P=19))

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))