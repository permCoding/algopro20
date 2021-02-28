class Student():
    def __init__(self, args):
        self.id = int(args[0])
        self.name = args[1]
        self.age = int(args[2])
        self.ball = float(args[3])
    def __str__(self):
        return '%3d %12s %4d %6.2f' % \
            (self.id, self.name, self.age, self.ball)


f = open('students.txt', 'r', encoding='utf-8')
lines = [line for line in f.read().split('\n')[1:] if len(line)>0]
f.close()

students = [Student(line.split('\t')) for line in lines]

for student in sorted(students, key=lambda st: st.ball, reverse=True):
    print(student)