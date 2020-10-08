file = open('task_4.txt', 'r')
lines = file.read().split('\n')
lines = list(filter(lambda line: len(line) > 0, lines))
file.close()

lst = []
for line in lines:
    lst.append(map(int, line.split('/')))

acc = 0
for item in lst:
    a, b = item
    print(a, b)
    acc += b
print(acc)