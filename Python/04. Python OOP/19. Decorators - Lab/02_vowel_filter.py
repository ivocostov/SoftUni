def vowel_filter(function):

    def wrapper():

        letters = function()
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowels_letter = [l for l in letters if l in vowels]

        return vowels_letter
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
