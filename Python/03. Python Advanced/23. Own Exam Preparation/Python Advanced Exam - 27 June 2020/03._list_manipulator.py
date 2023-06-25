def list_manipulator(*args):
    numbers_list = args[0]
    values = list(args[3:])


    if args[1] == 'add' and args[2] == 'beginning':
        numbers_list = values[0:] + numbers_list
        return numbers_list

    elif args[1] == 'add' and args[2] == 'end':
        numbers_list = numbers_list + values[0:]
        return numbers_list

    elif args[1] == 'remove' and args[2] == 'beginning':
        if values[0:]:
            numbers_list = numbers_list[values[-1]:]
        else:
            numbers_list.pop(0)
        return numbers_list

    elif args[1] == 'remove' and args[2] == 'end':
        if values[0:]:
            numbers_list = numbers_list[:-values[-1]]
        else:
            numbers_list.pop(-1)
        return numbers_list


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
