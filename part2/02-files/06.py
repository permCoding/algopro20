lines = []

with open('block.txt', mode='r', encoding='utf-8') as file:
    for line in file:
        lines.append(line[:-1])

# 
# 

print('\n'.join(lines))
