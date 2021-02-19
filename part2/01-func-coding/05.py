ages = [17, 21, 19]

agesS = sorted(ages)
print(agesS)
print(reversed(sorted(ages)))
print(list(reversed(sorted(ages))))

print('= = = = = = = = = =')

names = ['Оля', 'Аня', 'Яша']

students = list(zip(names, ages))
for student in students:
    print(student)

print('= = = = = = = = = =')

students.sort(key=lambda stud: stud[1])
for student in students:
    print(*student)

print('= = = = = = = = = =')

students.sort(key=lambda stud: stud[1], reverse=True)
for student in students:
    print(*student)

print('= = = = = = = = = =')

for student in sorted(students, key=lambda stud: stud[0]):
    print(*student)

