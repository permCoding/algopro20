with open('block.txt', mode='r', encoding='utf-8') as file:
    for line in file.read().split('\n'):
        print(line)
