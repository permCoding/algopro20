def print_fig_1(n):
    pos = 0
    for row in range(n):
        for col in range(n):
            pos += 1
            print(pos, '\t', end='')
        print()

def print_fig_2(n):
    for row in range(n):
        for col in range(n):
            pos = (col+1) + n*row
            print(pos, '\t', end='')
        print()


n = int(input())
print_fig_2(n)