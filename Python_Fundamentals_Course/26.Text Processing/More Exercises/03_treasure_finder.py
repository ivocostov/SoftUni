decryption_key = input().split()

decryption_key_index = 0
decrypted_message = ''

line = input()
while line != 'find':
    for symbol in line:
        if decryption_key_index >= len(decryption_key):
            decryption_key_index = 0
        result = ord(symbol) - int(decryption_key[decryption_key_index])
        decrypted_message += chr(result)
        decryption_key_index += 1

    if len(decrypted_message) == len(line):
        treasure_type = decrypted_message.split('&')[-2]
        temp_coordinates = decrypted_message.split('<')
        coordinates = ''
        for character in temp_coordinates[-1]:
            if character == '>':
                break
            else:
                coordinates += character
        print(f"Found {treasure_type} at {coordinates}")
        decryption_key_index = 0
        decrypted_message = ''

    line = input()

