def get_lines(name_file):
    file = open(name_file, 'r')
    lines = file.read().split('\n')
    lines = list(filter(lambda line: len(line) > 0, lines))
    file.close()
    return lines

def print_lines(lines):
    for line in lines:
        print(line)


lines = get_lines('task_4.txt')
print_lines(lines)

