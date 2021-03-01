lines = []

with open('block.txt', mode='r', encoding='utf-8') as file:
    lines = file.read().splitlines()

for line in reversed(list(filter(lambda line: len(line)>0, lines))): # в обратном порядке
    print(line)
