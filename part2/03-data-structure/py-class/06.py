class Student():
    def __init__(self, *args):
        self.id = args[0]
        self.name = args[1]
        self.age = args[2]
        self.ball = args[3]
    def __str__(self):
        return 'id =%3d name =%12s age =%3d ball = %.2f' % \
            (self.id, self.name, self.age, self.ball)


f = open('students.txt', 'r', encoding='utf-8')
lines = [line for line in f.read().split('\n')[1:] if len(line)>0]
f.close()

students = [Student(line.split('\t')) for line in lines]

for student in students:
    print(student)