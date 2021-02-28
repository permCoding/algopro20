# utf-8 для кириллицы

f = open('block.txt', encoding='utf-8')
txt = f.read()
f.close()

print(txt)
