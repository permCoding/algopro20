# ленивые вычисления

x = 0
y = 11
if x > 0 and y%2 != 0 and True:
    print('+ + +')
else:
    print('- - -')

# в Python 2 были два функции range и xrange
# range возвращала список, xrange - итератор
# в Python 3 осталась только ленивая range

# генераторы и итераторы


# генераторы
r = range(10) # возвращает объект-генератор
print(r) # где же сами значения ?
print(list(r))

print('- range -')
for item in r:
    print(item)
print('- range -')


def range_(n):
    i = 0
    while i < n:
        yield i
        i += 1


print('- yield -')
for item in range_(10):
    print(item)
print('- yield -')


def Fib(N):
    a, b = 1, 1
    for _ in range_(N):
        yield a
        a, b = b, a + b


print('- Fib -')
for next in Fib(10): # возвращает объект-генератор
    print(next)
print('- Fib -')

