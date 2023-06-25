from collections import deque


def climb_the_peaks(daily_portions, daily_stamina):
    conquered_peaks = []
    climbing_failed = False

    daily_portions, daily_stamina = deque(daily_food_portions), deque(stamina)
    list_of_peaks = {'Vihren': 80, 'Kutelo': 90, 'Banski Suhodol': 100, 'Polezhan': 60, 'Kamenitza': 70}

    for peak, climb_difficulty in list_of_peaks.items():
        while True:
            needed_climbing_stamina = int(daily_portions.pop()) + int(daily_stamina.popleft())

            if needed_climbing_stamina >= climb_difficulty:
                conquered_peaks.append(peak)
                break

            elif len(daily_portions) == 0 or len(daily_stamina) == 0:
                climbing_failed = True
                break

            if climbing_failed:
                if len(conquered_peaks) == 0:
                    return "Alex failed! He has to organize his journey better next time -> @PIRINWINS"
                else:
                    peaks_data = '\n'.join(conquered_peaks)
                    return f"Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK\nConquered peaks:\n{peaks_data}"


daily_food_portions = input().split(', ')
stamina = input().split(', ')

print(climb_the_peaks(daily_food_portions, stamina))



