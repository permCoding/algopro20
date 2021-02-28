file_r = open('block.txt', mode='r', encoding='utf-8')
lines = file_r.readlines()
file_r.close()

file_w = open('block-out.txt', mode='w', encoding='utf-8')
for line in lines:
    file_w.write(line)
file_w.close()
