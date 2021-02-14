ages = [17, 21, 19]
agesS = sorted(ages)
print(agesS)

names = ['Оля', 'Аня', 'Яша']

students = list(zip(names, ages))
for student in students:
    print(student)

students.sort(key=lambda stud: stud[1])
for student in students:
    print(student)

students.sort(key=lambda stud: stud[1], reverse=True)
for student in students:
    print(student)

for student in sorted(students, key=lambda stud: stud[0]):
    print(student)


a = [21, 22, 23, 22]
n = ['Zzz','Xxx','Yyy','Aaa']
lst = list(zip(n, a))
lst.sort(key=lambda item: (
        item[1],
        item[0]
    )
)
for item in lst:
    print(item[1], item[0])


from itertools import groupby

result = []
for key, group in groupby(lst, lambda item: item[1]):
    print(key)
    result += [item for item in group]
for item in result:
    print(item[1], item[0])

result = []
for key, group in groupby(sorted(lst, key=lambda item: item[1]), lambda item: item[1]):
    result += [item for item in sorted(group, key=lambda item: item[0], reverse=True)]
for item in result:
    print(item[1], item[0])
