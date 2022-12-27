tail = input()
body = input()
head = input()


animal_parts_list = [tail, body, head]
animal_parts_list[0], animal_parts_list[2] = animal_parts_list[2], animal_parts_list[0]
print(animal_parts_list)
