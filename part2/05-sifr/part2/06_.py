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


name_image = 'xy_белка.bmp'
img = Image.open(name_image)
width, height = img.size # исходные размеры рисунка
rastr = img.load()

result = ''
ns = 0; x = 0; y = 0 # от этой точки будем начинать
while ns < 100:
    pos_b = ''
    for shift in range(8): # это сдвиг по битам символа
        (r,g,b) = rastr[x, y]
        pos_b += str(b&1)
        x += 1
        if x == width:
            x = 0
            y += 1
    pos = int(pos_b[::-1], 2)
    ns += 1
    # print(pos)
    alph = get_alph()
    result += alph[pos]

print(result)
