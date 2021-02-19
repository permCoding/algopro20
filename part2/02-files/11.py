lines = []

with open('block.txt', mode='r', encoding='utf-8') as file:
    lines = file.read().splitlines()

while lines:
    print(lines.pop())