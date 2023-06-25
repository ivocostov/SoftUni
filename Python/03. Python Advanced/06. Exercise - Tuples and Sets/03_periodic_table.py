count_of_input_lines = int(input())

list_of_chemicals = set()

for chemical_element in range(count_of_input_lines):
    chemical_compounds = input().split()
    for element in chemical_compounds:
        list_of_chemicals.add(element)

print(*list_of_chemicals, sep='\n')
