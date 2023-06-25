def numbers_searching(*args):
    duplicate_numbers = set()
    initial_list = []
    starting_number = min(args)
    end_number = max(args)
    start_index = 0
    resulting_list = []

    for element in range(starting_number, end_number + 1):
        initial_list.append(element)

    for missing_num in initial_list:
        if missing_num != args[start_index] and missing_num not in args:
            resulting_list.append(missing_num)
            break
        else:
            start_index += 1

    for duplicate_num in args:
        result = args.count(duplicate_num)
        if result < 2:
            continue
        else:
            duplicate_numbers.add(duplicate_num)

    resulting_list.append(sorted(list(duplicate_numbers)))

    return resulting_list


#print(numbers_searching(1, 2, 4, 2, 5, 4))
#print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))