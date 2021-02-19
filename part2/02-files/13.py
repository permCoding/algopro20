file_r = open('block.txt', mode='r', encoding='utf-8')
txt = file_r.read()
file_r.close()

file_w = open('block-out.txt', mode='w', encoding='utf-8')
file_w.write(txt)
file_w.close()