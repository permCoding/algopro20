lines = []

with open('block.txt', mode='r', encoding='utf-8') as file:
    lines = file.read().splitlines()

for line in lines:
    print(line)