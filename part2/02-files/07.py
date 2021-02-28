with open('07.py', mode='r', encoding='utf-8') as file:
    for num, line in enumerate(file, 1):
        print(f'{num}\t{line[:-1]}')

