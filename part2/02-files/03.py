f = open('block.txt', mode='r', encoding='utf-8')
txt = f.read()
f.close()

lines = txt.split('\n')
for line in lines:
    print(line)