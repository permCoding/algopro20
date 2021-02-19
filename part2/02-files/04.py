lines = []

with open('block.txt', mode='r', encoding='utf-8') as file:
    lines = file.read().split('\n')

for line in lines:
    print(line)