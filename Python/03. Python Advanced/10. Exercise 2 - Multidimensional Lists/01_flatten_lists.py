user_input = input().split('|')

output_list = []
final_list = []

for sequence in user_input:
    stripped_sequence = sequence.strip()
    output_list.append(stripped_sequence.split())

output_list.reverse()

for inner_list in output_list:
    for symbol in inner_list:
        final_list.append(symbol)

print(*final_list)
