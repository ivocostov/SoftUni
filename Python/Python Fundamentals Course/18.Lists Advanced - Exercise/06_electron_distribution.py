number_of_electrons = int(input())

shells = []
current_shell = 0

while True:
    current_shell += 1
    electrons_to_be_filled = 2 * (current_shell ** 2)
    if number_of_electrons - electrons_to_be_filled >= 0:
        shells.append(electrons_to_be_filled)
        number_of_electrons -= electrons_to_be_filled
        if number_of_electrons == 0:
            break
    if number_of_electrons - electrons_to_be_filled < 0:
        shells.append(abs(number_of_electrons))
        break

print(shells)
