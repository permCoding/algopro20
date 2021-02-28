numbers = {
    ' *** * *': 1,
    '** ** **': 2
}

f = open('05.txt')
lines = f.read().splitlines()
key = ''.join(lines)

print(numbers[key])
