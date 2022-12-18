number_of_jury_members = int(input())

number_of_presentations = 0
average_grade = 0
presentation_name = input()

while presentation_name != "Finish":
    current_presentation_name = presentation_name
    number_of_presentations += 1
    current_presentation_grade = 0
    for presentation_grade in range(number_of_jury_members):
        current_grade = float(input())
        current_presentation_grade += current_grade
    current_presentation_grade /= number_of_jury_members
    print(f"{current_presentation_name} - {current_presentation_grade:.2f}.")
    average_grade += current_presentation_grade

    presentation_name = input()

average_grade /= number_of_presentations
print(f"Student's final assessment is {average_grade:.2f}.")
