numbers = {
    ' *** * *': 1,
    '** ** **': 2
}

f = open('06.txt')
lines = f.read().splitlines()
keys = [''.join(lines[num:num+4]) for num in range(0, len(lines), 4)]

for key in keys:
    print(numbers[key])
