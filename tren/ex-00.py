import random as r

n = 1000
lst = [r.randint(1, 100) for _ in range(n)]

lines = list(map(str, lst))

line = ' '.join(lines)

f = open('data_line.txt', 'w')
f.write(line)
f.close()

lines = [line + '\n' for line in lines]
f = open('data_lines.txt', 'w')
f.writelines(lines)
f.close()
