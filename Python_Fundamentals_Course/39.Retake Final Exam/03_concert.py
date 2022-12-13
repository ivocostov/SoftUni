members_dictionary = {}
time_to_play_dict = {}
play_time_str, band_members_str = 'play time', 'band members'


def play(name_of_band, play_time):
    if name_of_band not in time_to_play_dict.keys():
        time_to_play_dict[name_of_band] = [play_time]
    else:
        time_to_play_dict[name_of_band].append(play_time)


def add(name_of_band, members):
    new_members = members.split(', ')
    if name_of_band not in members_dictionary.keys():
        members_dictionary[name_of_band] = []
        for current_member in new_members:
            if current_member not in members_dictionary[name_of_band]:
                members_dictionary[name_of_band].append(current_member)
    else:
        for current_member in new_members:
            if current_member not in members_dictionary[name_of_band]:
                members_dictionary[name_of_band].append(current_member)


def results():
    total_playing_time = 0
    for key, value in time_to_play_dict.items():
        for time in value:
            total_playing_time += int(time)

    print(f"Total time: {total_playing_time}")
    for band, playtime in time_to_play_dict.items():
        print(f"{band} -> {sum(playtime)}")

    first_band = list(members_dictionary.keys())[0]
    print(first_band)

    for current_band, current_members in members_dictionary.items():
        if current_band == first_band:
            for member in current_members:
                print(f"=> {member}")


while True:
    bands_info = input()
    if bands_info == 'Start!':
        break

    current_band_info = bands_info.split('; ')
    command = current_band_info[0]

    if command == 'Play':
        band_name = current_band_info[1]
        time_to_play = int(current_band_info[2])
        play(band_name, time_to_play)
    elif command == 'Add':
        band_name = current_band_info[1]
        band_members = current_band_info[2]
        add(band_name, band_members)


results()
