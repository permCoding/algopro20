file = open('block.txt', mode='r', encoding='utf-8')

result = ''
k = 25 # кол-во байт для чтения за один раз
line = file.readline(k)
while line:
    result += line
    line = file.readline(k)
print(result)

file.close()
