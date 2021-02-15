# анонимные функции

get1 = lambda n: divmod(n, 2)
# d, m = lambda n: divmod(n, 2) # так нельзя

d, m = get1(7)
print(f'd = {d}; m = {m}')

# # # # # # # # # # # # # # # # #
# map
# filter
# reduce

s = '123456'
lstStr = list(s)

def getInt1(smb):
    return int(smb)

getInt2 = lambda smb: int(smb)

lstNum = map(getInt1, lstStr) # map
print(list(lstNum))
lstNum = map(getInt2, lstStr) # map
print(list(lstNum))
lstNum = map(lambda smb: int(smb), lstStr) # map
print(list(lstNum))
lstNum = map(int, lstStr) # map
print(list(lstNum))


lstEven = list(filter(lambda item: int(item)%2 == 0, lstStr)) # filter
print(lstEven)

from functools import reduce

# reduce
summa = reduce(lambda acc, next: acc + next, map(int, lstStr), 0) 
print(summa)

# [1, 2, 3, 4, 5, 6]
# acc = 0
# acc next