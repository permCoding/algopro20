import math

def get_sin(x, q):
    p = 1; sign = 1; sin_x = 0; sin_old = 0
    while True:
        sin_x += sign * (x**p/math.factorial(p))
        p += 2; sign = -sign
        if abs(sin_x-sin_old) <= q:
            return sin_x
        sin_old = sin_x    

g = float(input('введите угол в градусах - '))
x = g*math.pi/180
q = float(input('введите q - '))
# print(f'ответ = {get_sin(x, q)}')
print('ответ = %.3f' % get_sin(x, q))
# 'строка для вывода с позициями'.format(аргументы)