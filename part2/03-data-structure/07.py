numbers = {
    ' *** * *': 1,
    '** ** **': 2
}

line = ' *\n**\n *\n *'
key = ''.join(line.split('\n'))
print(numbers[key])
