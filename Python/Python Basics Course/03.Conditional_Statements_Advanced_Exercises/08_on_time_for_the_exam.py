hour_of_exam = int(input())
minutes_of_exam = int(input())
hour_of_arrival = int(input())
minutes_of_arrival = int(input())


hour_of_exam_to_minutes = hour_of_exam * 60 + minutes_of_exam
hour_of_arrival_to_minutes = hour_of_arrival * 60 + minutes_of_arrival


time_difference = abs(hour_of_arrival_to_minutes - hour_of_exam_to_minutes)

hour = time_difference // 60
minutes = time_difference % 60

if minutes == 60:
    minutes = 0
if hour == 24:
    hour = 0

if hour_of_arrival_to_minutes == hour_of_exam_to_minutes:
    print("On time")
elif hour_of_exam_to_minutes - 60 >= hour_of_arrival_to_minutes:
    print("Early")
    print(f"{hour}:{minutes:02d} hours before the start")
elif hour_of_exam_to_minutes - 30 > hour_of_arrival_to_minutes:
    print("Early")
    print(f"{minutes} minutes before the start")
elif hour_of_exam_to_minutes - 30 <= hour_of_arrival_to_minutes <= hour_of_exam_to_minutes:
    print("On time")
    print(f"{minutes} minutes before the start")
elif hour_of_arrival_to_minutes >= hour_of_exam_to_minutes + 60:
    print("Late")
    print(f"{hour}:{minutes:02d} hours after the start")
elif hour_of_exam_to_minutes < hour_of_arrival_to_minutes <= hour_of_exam_to_minutes + 59:
    print("Late")
    print(f"{minutes} minutes after the start")




