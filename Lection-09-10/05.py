file = open('task_4.txt', 'r')
lines = file.readlines()
file.close()

# ver.1
# def last_del(s):
#     return s[:-1]

# lines = list(map(last_del, lines))

# ver.2
lines = list(map(lambda line: line[:-1], lines))

for line in lines:
    print(line)

print(lines)