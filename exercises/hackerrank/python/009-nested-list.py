if __name__ == '__main__':
    students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    scores = sorted(students, key=lambda x: x[1])

    lowest_score = scores[0][1]

    second_lowest_score = None
    for student in scores:
        if student[1] > lowest_score:
            second_lowest_score = student[1]
            break

    second_lowest_students = [name for name, score in students if score == second_lowest_score]

    for student in sorted(second_lowest_students):
        print(student)
