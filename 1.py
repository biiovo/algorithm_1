# 获取总的测试轮数
num_rounds = int(input())

for round_idx in range(num_rounds):

    student_numbers = int(input())

    nearly_late_students = 0

    absentee_students = 0

    student_times = []
    for student_idx in range(student_numbers):

        time_input = input()

        hour_component, minute_component = map(int, time_input.split(":"))

        total_minutes = hour_component * 60 + minute_component
        student_times.append(total_minutes)


    for minutes in student_times:
        if minutes > 8 * 60 + 5:
            absentee_students += 1

    for minutes in student_times:
        if 8 * 60 < minutes <= 8 * 60 + 5:
            nearly_late_students += 1

    print(nearly_late_students, absentee_students)