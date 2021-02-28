file = open('block.txt', mode='r', encoding='utf-8')

result = ''
k = 25 # кол-во байт для чтения за один раз
chunk = file.readline(k)
while chunk:
    result += chunk
    chunk = file.readline(k)
print(result)

file.close()
