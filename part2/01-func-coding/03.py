# ленивые вычисления

x = 0
y = 11
if x > 0 and y%2 != 0 and True:
    print('+')
else:
    print('-')

# в Python 2 были два функции range и xrange
# range возвращала список, xrange - итератор
# в Python 3 осталась только ленивая range

# генераторы и итераторы


# генераторы
r = range(10) # возвращает объект-генератор
print(r) # где же сами значения ?
print(list(r))
for item in r:
    print(item)


def Fib(N):
    a, b = 1, 1
    for _ in range(N):
        yield a
        a, b = b, a + b


for next in Fib(5): # возвращает объект-генератор
    print(next)


# итераторы
lst = list(range(10)) # объект-итератор
print(lst)
lst = [smb for smb in '012345']
print(lst)

enum = [smb for smb in enumerate([1,4,55,9])]
print(enum)

for index, value in enumerate('Python'):
    print(index, value)
