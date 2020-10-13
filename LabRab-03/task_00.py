
n = 5
s = '*' * n
for i in range(n):
    print(s)

# lst = [1, 2, 3]
# print(lst)
# print(*lst)
# [1, 2, 3]
# 1 2 3

n = 7
lst = []
for i in range(1, n+1):
    lst.append(i)
    # lst += [i]
    print(*lst)
    # print(' '.join(map(str, lst)))