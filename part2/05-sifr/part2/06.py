# прочитаем один символ из несколько подряд идущих пикселей

from PIL import Image

def get_alph():
    eng = 'abcdefghijklmnopqrstuvwxyz'
    rus = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    nums = '1234567890'
    smbs = ':; !&-+=()*/.,_{}[]#№'
    arr = [chr(9), chr(13), chr(10)]
    alph = rus + rus.upper() + eng + eng.upper() + nums + smbs + ''.join(arr)
    return alph


def get_bit(pos, shift):
    mask = 1 << shift
    sign = (pos & mask) >> shift
    return sign




name_image = '0_белка.bmp'
img = Image.open(name_image)
rastr = img.load()

x = 0; y = 0 # от этой точки будем начинать
shift = 0 # это сдвиг по битам символа
pos_b = ''
for p in range(3):
    (r,g,b) = rastr[x, y]
    pos_b += str(r&1); shift += 1
    pos_b += str(g&1); shift += 1
    pos_b += str(b&1); shift += 1
    x += 1

pos = int(pos_b[::-1], 2)
print(pos)

alph = get_alph()
print(alph[pos])
