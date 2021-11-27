jury = int(input())
command = input()
final_grade = 0
counter_if_exams = 0
while command != 'Finish':
    presentation_name = command
    middle_grade = 0
    for grade in range(jury):
        current_grade = float(input())
        middle_grade += current_grade
        counter_if_exams += 1
        final_grade += current_grade
    middle_grade /= jury
    print(f"{presentation_name} - {middle_grade:.2f}.")
    command = input()
final_grade /= counter_if_exams
print(f"Student's final assessment is {final_grade:.2f}.")