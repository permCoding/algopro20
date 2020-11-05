s = '1 2 0 3 4 9 9 -4 8 0 1 6 5 7 0 9 9 -4 8 0 1 6 5 7 0'
lst = list(map(int, s.split()))
n = int(len(lst)** .5)
tab = [lst[y*5:y*5+5] for y in range(n)]

acc = 0
for y in range(n):
    for x in range(n):
        if x == y:
            acc += tab[y][x]
print(acc)
# n**2 - это плохо
# n - это хорошо
acc = 0
for i in range(n):
    acc += tab[i][i]
print(acc)