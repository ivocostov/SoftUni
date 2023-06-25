clothes_in_each_box = [int(x) for x in input().split()]
rack_capacity = int(input())

temp_sum = rack_capacity
racks_needed = 1    # тук е единица защото се започва от първи рафт не може да се каже че започваш от нула рафт

while clothes_in_each_box:
    last_cloth = clothes_in_each_box.pop()

    if temp_sum - last_cloth >= 0:
        temp_sum -= last_cloth
    else:
        racks_needed += 1
        temp_sum = rack_capacity - last_cloth  # тук е - last_cloth, защото на горния ред вече сме взели новия рафт и текущата дреха се закача на него( новият рафт )


print(racks_needed)
