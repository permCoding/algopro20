# pip3 install pillow
# как узнать rgb-компоненты цвета пикселя

from PIL import Image

img = Image.open("color.jpg")

width, height = img.size

point1 = (0, 0)
point2 = (width-1, 0)
point3 = (0, height-1)
point4 = (width-1, height-1)

points = [point1, point2, point3, point4]

for point in points:
    color = img.getpixel(point)
    r, g, b = color
    print(f'r = {r}, g = {g}, b = {b}')
