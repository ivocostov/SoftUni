def swap_elements(array_values, index1, index2):
    array_values[index1], array_values[index2] = array_values[index2], array_values[index1]
    return array_values


def multiply_elements(array_values, index1, index2):
    answer = array_values[index1] * array_values[index2]
    array_values.pop(index1)
    array_values.insert(index1, answer)
    return array_values


def decrease_elements(array_values):
    for index, current_element in enumerate(array_values):
        current_element -= 1
        array_values.insert(index, current_element)
        array_values.pop(index + 1)
    return array_values


def array_modifier(array_values):
    while True:
        user_command = input()

        if user_command == 'end':
            break

        if user_command == 'decrease':
            result = decrease_elements(array_values)
            break
            
        given_command, index1, index2 = user_command.split()

        if given_command == 'swap':
            result = swap_elements(array_values, int(index1), int(index2))

        elif given_command == 'multiply':
            result = multiply_elements(array_values, int(index1), int(index2))

    result = ', '.join([str(num) for num in array_values])
    print(result)


initial_array_values = list(map(int, input().split()))
array_modifier(initial_array_values)
