import math

g = int(input())
q = float(input())
x = math.pi/180 * g
p = 1; z = 1; sin_x = 0; step = q + 1
while abs(step) > q:
    step = z * (x**p / math.factorial(p))
    p += 2; z = -z; sin_x += step

print('sin = %.3f' % sin_x)