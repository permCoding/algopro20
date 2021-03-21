# переходим на формат файла bmp
# как глубока кроличья нора?

from PIL import Image


name_image = 'белка.bmp'
img = Image.open(name_image)

rastr = img.load()

x = 5; y = 5

color = rastr[x, y]
print(color)

r, g, b = color

bit = 7 # испытываем какой бит можно испортить
shift = 1 << bit
print(shift)
r -= shift; g -= shift; b -= shift

color = (r, g, b)
rastr[x, y] = color

img.save('_' + name_image)
img.show()
