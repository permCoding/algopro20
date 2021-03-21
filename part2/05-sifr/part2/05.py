# запишем один символ в несколько подряд идущих пикселей

from PIL import Image

def get_alph():
    eng = 'abcdefghijklmnopqrstuvwxyz'
    rus = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    nums = '1234567890'
    smbs = ':; !&-+=()*/.,_{}[]#№'
    arr = [chr(9), chr(13), chr(10)]
    alph = rus + rus.upper() + eng + eng.upper() + nums + smbs + ''.join(arr)
    return alph


def get_text(file_name):
    with open(file_name, mode='r', encoding='utf-8') as f:
        text = f.read()
    return text


def get_bit(pos, shift):
    mask = 1 << shift
    sign = (pos & mask) >> shift
    return sign


alph = get_alph()
text = get_text('block.txt')

smb = text[0]
pos = alph.find(smb)
print(pos)

name_image = 'белка.bmp'
img = Image.open(name_image)
rastr = img.load()

x = 0; y = 0 # от этой точки будем начинать
shift = 0 # это сдвиг по битам символа

for p in range(3):
    (r,g,b) = rastr[x, y]
    r = (r & 254) | get_bit(pos, shift); shift += 1
    g = (g & 254) | get_bit(pos, shift); shift += 1
    b = (b & 254) | get_bit(pos, shift); shift += 1
    rastr[x,y] = (r,g,b)
    x += 1

img.save('0_' + name_image)
