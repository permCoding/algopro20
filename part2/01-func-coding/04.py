# генераторы и итераторы

# итераторы
lst = list(range(10)) 
print(lst) # объект-итератор

lst = [smb for smb in '012345']
print(lst) # объект-итератор

lst = (smb for smb in '012345')
print(lst) # объект-генератор
print(', '.join(lst))

print('= = = = = = = = =')

tpl = (x for x in [0, 1, 2, 3]) # из итератора в генератор
print(tpl)
# print(list(tpl))
print(next(tpl))
print(next(tpl))
print(next(tpl))
print(next(tpl))
print(tpl)

print('= = = = = = = = =')

enum = [smb for smb in enumerate([1, 4, 55, 9])]
print(enum)

for index, value in enumerate('Python'):
    print(index, value)
