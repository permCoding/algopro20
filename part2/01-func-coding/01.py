# именованные функции

def get1(n):
    '''
    функция может возвращать более чем 1 аргумент
    в реальности возвращается один объект - кортеж
    '''
    return divmod(n, 2)


def get2(n, b=2):
    '''
    необязательный аргумент со значением по умолчанию
    '''
    return divmod(n, b)


def get3(*args):
    '''
    неизвестное кол-во аргументов, записанное через ,
    '''
    return max(args) - min(args)


def get4(**kwargs):
    '''
    именованные аргументы
    '''
    for key, value in kwargs.items():
        print("{} = {}".format(key, value))


def get5(**kwargs):
    '''
    именованные аргументы
    '''
    return divmod(kwargs['d'], kwargs['m'])
    
def get_bin(n):
    ''' перевод в 2-ую СС '''
    digits = []
    while n > 0:
        n, d = divmod(n, 2)
        digits.append(d)
    return ''.join(map(str, reversed(digits)))


kg = get1(7)
print(kg)

a, b = 22, 33
a, b = b, a
print(a, b)

d, m = get1(7)
print(f'd = {d}; m = {m}')

d, m = get2(7)
print(f'd = {d}; m = {m}')

d, m = get2(7, 10)
print(f'd = {d}; m ={m}')

print('dif = %d' % get3(7, 3, 66, 9, 1))
print('dif = %d' % get3(7, 2))
args = (7, 2, 9)
print('dif = %d' % get3(*args))

get4(d=7, m=2)
print(get5(d=7, m=2))

print(get_bin(14))