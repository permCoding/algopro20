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

name_image = 'белка.bmp'
img = Image.open(name_image)
width, height = img.size # исходные размеры рисунка
rastr = img.load()


x = 0; y = 0; ns = 0 # number symbol 
while ns < len(text):

    smb = text[ns]
    pos = alph.find(smb)
    print(pos)

    for shift in range(8): # это сдвиг по битам символа
        (r,g,b) = rastr[x, y]
        b = (b & 254) | get_bit(pos, shift)
        rastr[x,y] = (r,g,b)
        x += 1
        if x == width:
            x = 0
            y += 1
    ns += 1

img.save('xy_' + name_image)
