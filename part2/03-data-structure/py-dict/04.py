numbers = {
    1: ' *** * *',
    2: '** ** **'
}

def getImageNum(line):
    lst = [line[i: i+2] for i in range(0, len(line), 2)]
    return '\n'.join(lst)

print(getImageNum(numbers[1]))
print(getImageNum(numbers[2]))