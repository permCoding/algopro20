import random
import os

os.system('cls')

def gen_random_set(count):
    st = set()
    while len(st) < count:
        st.add(random.randint(0, 9))
    return list(st)


n = 4
for _ in range(10):
    print(gen_random_set(n))

