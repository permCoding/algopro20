# последовательность Фибоначчи
# 1 1 2 3 5 8 13 21 34 55 ...

def Fib1(n):
    if n == 1 or n == 2:
        return 1
    else:
        return Fib1(n-2) + Fib1(n-1)


tab = [0, 1, 1]
def Fib2(n):
    if n == 1 or n == 2:
        return 1
    else:
        if tab[n-2] == 0:
            tab[n-2] = Fib2(n-2)
        if tab[n-1] == 0:
            tab[n-1] = Fib2(n-1)
        return tab[n-2] + tab[n-1]


print(Fib1(36))

n = 72
tab += [0] * n
print(Fib2(n))
