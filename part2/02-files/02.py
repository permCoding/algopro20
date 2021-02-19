f = open('block.txt', mode='r', encoding='utf-8')
lines = f.readlines()
f.close()

for line in lines:
    # print(line[:-1])
    print(line.rstrip('\n'))