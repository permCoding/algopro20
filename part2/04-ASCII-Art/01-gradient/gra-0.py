# pip3 install pillow
# как узнать rgb-компоненты цвета одного пикселя

from PIL import Image

img = Image.open("white.jpg")

point = (0, 0)

color = img.getpixel(point)

r, g, b = color

print(f'r = {r}, g = {g}, b = {b}')
