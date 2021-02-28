from module import Point, get_lines


lines = get_lines('points.txt', 1)
points = [Point(tuple(map(int, line.split('\t')))) for line in lines]

for point in points:
    point.move('ne')
    print(point)
