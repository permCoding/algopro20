n = int(input())

# for row in range(1, n+1):
#     for col in range(1, row+1):
#         print(col, end='')
#     print()

# for row in range(1, n + 1):
#     g = [str(col) for col in range(1, row+1)]
#     print(' '.join(g))

for row in range(1, n + 1):
    print(' '.join(map(str, range(1, row+1))))


# for i in range(n):
#     print(i, end='')
#     print('X'*n)
#     # for j in range(n):
#     #     print('X', end='')
#     # print()
