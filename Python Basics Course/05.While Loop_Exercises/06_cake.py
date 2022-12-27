cake_width = int(input())
cake_longitude = int(input())
total_pieces = cake_width * cake_longitude
no_more_pieces_left = False

while total_pieces > 0:
    command = input()
    if command == 'STOP':
        print(f"{total_pieces} pieces are left.")
        break

    pieces_taken = int(command)
    total_pieces -= pieces_taken

    if total_pieces <= 0:
        no_more_pieces_left = True
        break

if no_more_pieces_left:
    print(f"No more cake left! You need {abs(total_pieces)} pieces more.")
