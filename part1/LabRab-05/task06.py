def square(length):
    sm = (size - length) // 2
    for i in range(length):
        tab[sm+0][sm+i] = 'X'
    for i in range(length):
        tab[sm+length-1][sm+i] = 'X'
    for i in range(length):
        tab[sm+i][sm+0] = 'X'
    for i in range(length):
        tab[sm+i][sm+length-1] = 'X'

def rec(r):
    if r == 1:
        tab[0][0] = 'X'  # самостоятельно / size
    else:
        square(r)    
        rec(r - 4)


n = 9
size = n*2 - 1
tab = [[' ' for col in range(size)] for row in range(size)]

rec(size)

for row in tab:
    print(*row)
