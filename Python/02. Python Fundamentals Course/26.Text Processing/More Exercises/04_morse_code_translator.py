<<<<<<< HEAD
morse_code_dictionary = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
                         'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
                         'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
                         'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
                         '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
                         '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
                         '(': '-.--.', ')': '-.--.-'}

translated_message = ''
temporary = ''

input_morse_code = input().split(' | ')

for index in range(len(input_morse_code)):
    temp_sign = input_morse_code[index].split()
    for index_1 in range(len(temp_sign)):
        current_sign = temp_sign[index_1]
        for letter, morse_sign in morse_code_dictionary.items():
            if morse_sign == current_sign:
                translated_message += letter
    translated_message += ' '


=======
morse_code_dictionary = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
                         'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
                         'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
                         'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
                         '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
                         '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
                         '(': '-.--.', ')': '-.--.-'}

translated_message = ''
temporary = ''

input_morse_code = input().split(' | ')

for index in range(len(input_morse_code)):
    temp_sign = input_morse_code[index].split()
    for index_1 in range(len(temp_sign)):
        current_sign = temp_sign[index_1]
        for letter, morse_sign in morse_code_dictionary.items():
            if morse_sign == current_sign:
                translated_message += letter
    translated_message += ' '


>>>>>>> 36496de6931529b811d0c463d6ad38e232c5703a
print(translated_message)