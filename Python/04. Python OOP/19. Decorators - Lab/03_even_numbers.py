def even_numbers(function):

    def wrapper(numbers):
        numbers_list = function(numbers)
        even_numbers = [n for n in numbers_list if n % 2 == 0]
        return even_numbers
    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))
