file = open('task_4.txt', 'r')
lines = file.read().split('\n')
file.close()

lines = list(filter(lambda line: len(line) > 0, lines))

acc = 0
for line in lines:
    a, b = line.split('/')
    acc += int(a) / int(b)

print(acc)

