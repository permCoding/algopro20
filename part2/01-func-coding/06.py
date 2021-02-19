a = [21, 22, 23, 22, 22]
n = ['Zzz','Xxx','Yyy','Aaa', 'Ooo']
lst = list(zip(n, a))
lst.sort(key=lambda item: (
        # item[1],
        -item[1],
        item[0]
    )
)
for item in lst:
    print(item[1], item[0])

print('= = = = = = = = = =')

from itertools import groupby

result = []
for key, group in groupby(lst, lambda item: item[1]):
    # print(f'key = {key}, group = {list(group)}')
    print(f'key = {key}, group = {group}')
    result += [item for item in group]
for item in result:
    print(item[1], item[0])

print('= = = = = = = = = =')

result = []
for key, group in groupby(lst, lambda item: item[1]):
    result += [item for item in sorted(group, key=lambda item: item[0], reverse=True)]
for item in result:
    print(item[1], item[0])
