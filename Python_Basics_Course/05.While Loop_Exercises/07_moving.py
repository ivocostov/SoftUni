available_space_width = int(input())
available_space_longitude = int(input())
available_space_height = int(input())
total_area_available = available_space_width * available_space_longitude * available_space_height
no_more_space_available = False

while total_area_available > 0:
    command = input()
    if command == "Done":
        print(f"{total_area_available} Cubic meters left.")
        break

    boxes_to_be_moved = int(command)
    total_area_available -= boxes_to_be_moved

    if total_area_available <= 0:
        no_more_space_available = True
        break

if no_more_space_available:
    print(f"No more free space! You need {abs(total_area_available)} Cubic meters more.")
