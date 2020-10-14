# КОНТРОЛЬНАЯ ЗАДАЧА 2
# ИСПОЛЬЗУЯ ТИП ДАННЫХ МНОЖЕСТВО 
# СГЕНЕРИРУЙТЕ СПИСОК ИЗ 4-Х НЕПОВТОРЯЮЩИХСЯ ЦИФР (ОТ 0 ДО 9)
# ТАКОЕ, НАПРИМЕР, НАДО В ИГРЕ "БЫКИ-КОРОВЫ"

import random
import sys
import os

os.system('cls')

print(sys.maxsize)

# lst = [1, 2, 3, 4]
# random.shuffle(lst)
# print(lst)

st = set()

# ver.1
# for _ in range(4, 2**16):
#     st.add(random.randint(0, 9))
#     if len(st) == 4:
#         break

while len(st) < 4:
    st.add(random.randint(0, 9))

lst = list(st)
print(lst)