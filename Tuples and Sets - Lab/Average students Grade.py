students_info = {}

for _ in range(int(input())):
    name, grade = input().split()
    if name not in students_info:
        students_info[name] = [float(grade)]
    else:
        students_info[name].append(float(grade))

for student, grades in students_info.items():
    average = sum(float(grade) for grade in grades) / len(students_info[student])
    grades = [f"{n:.2f}" for n in grades]
    print(f"{student} -> {' '.join(grades)} (avg: {average:.2f})")
