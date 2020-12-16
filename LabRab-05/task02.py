f = open('input.txt')
n = int(f.readline())
# print(n)

count = 0
for row in range(n):
    line = f.readline()
    count += line.count('1')

print(count//2)