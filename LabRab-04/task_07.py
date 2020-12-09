def terminator(line):
    return line[:-1]


def get_lines(name_file):
    f = open(name_file)
    lines = f.readlines()
    f.close()

    # ver.1
    # lines_new1 = []
    # for line in lines:
    #     lines_new.append(line[:-1])
    # ver.2
    # lines_new1 = list(map(terminator, lines))
    # ver.3
    lines_new1 = list(map(lambda line: line[:-1], lines))

    # ver.1
    # lines_new2 = []
    # for line in lines_new1:
    #     if line != '':
    #         lines_new2.append(line)
    # ver.3
    lines_new2 = list(filter(lambda line: line != '', lines_new1))

    return lines_new2


def get_table(lines):
    # lst = [num**2 for num in range(10) if num % 2 != 0]
    tab = []
    for line in lines:
        tab.append(list(map(int , line.split())))
    return tab


def print_table(tab):
    for row in tab:
        print(*row)


def get_trans(tab):
    n = len(tab)
    for row in range(n):
        for col in range(n):
            if col > row:
                tab[row][col], tab[col][row] = tab[col][row], tab[row][col]
    return tab

lines = get_lines('input.txt')
tab = get_table(lines)
print_table(tab)
print()
tab = get_trans(tab)
print_table(tab)