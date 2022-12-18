<<<<<<< HEAD
start_symbol = input()
end_symbol = input()
current_string = input()
characters_ascii_code_sum = 0
ascii_code_list = []

start_symbol_ascii_code = ord(start_symbol)
end_symbol_ascii_code = ord(end_symbol)

for symbol in current_string:
    current_ascii_code = ord(symbol)
    if start_symbol_ascii_code < current_ascii_code < end_symbol_ascii_code:
        ascii_code_list.append(current_ascii_code)

print(sum(ascii_code_list))

=======
start_symbol = input()
end_symbol = input()
current_string = input()
characters_ascii_code_sum = 0
ascii_code_list = []

start_symbol_ascii_code = ord(start_symbol)
end_symbol_ascii_code = ord(end_symbol)

for symbol in current_string:
    current_ascii_code = ord(symbol)
    if start_symbol_ascii_code < current_ascii_code < end_symbol_ascii_code:
        ascii_code_list.append(current_ascii_code)

print(sum(ascii_code_list))

>>>>>>> 36496de6931529b811d0c463d6ad38e232c5703a
