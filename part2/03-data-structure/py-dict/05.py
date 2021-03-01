
numbers = {
    ' *** * *': 1,
    '** ** **': 2
}

f = open('05.txt')
lines = f.read().splitlines()
f.close()

key = ''.join(lines)

print(numbers[key])
