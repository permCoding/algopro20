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
lstStr = s.split()

def getInt1(smb):
    return int(smb)

getInt2 = lambda smb: int(smb)

lstNum = [] # map
lstEven = [] # filter
summa = 0 # reduce

from functools import reduce

# 