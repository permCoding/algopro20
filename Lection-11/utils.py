def get_lines(name_file):
    '''
    прочитать файл, вернуть список строк
    '''
    file = open(name_file, 'r')
    lines = file.read().split('\n')
    lines = list(filter(lambda line: len(line) > 0, lines))
    file.close()
    return lines


def print_lines(lines):
    """
    вывести список строк построчно в столбик
    """
    for line in lines:
        print(line)


