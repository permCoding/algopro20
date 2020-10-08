# 2/1 + 2/3 + 4/3 + 4/5 + 6/5 + 6/7

name_file = 'task_4.txt'

n = 9

a, b = 2, 1

file = open(name_file, 'w')
for i in range(n):
    tmp = str(a) + '/' + str(b)
    file.write(tmp + '\n')
    if i % 2 != 0:
        a += 2
    else:
        b += 2
    

file.close()

