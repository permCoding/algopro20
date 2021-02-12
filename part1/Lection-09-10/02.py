import os
import sys

os.system('cls')

path = os.getcwd()

files = os.listdir(path)

print(files)

for file in files:
    print(file)

char = '\n'
print(ord(char))

char = chr(13)
print(char.join(files))

# with open('input.txt', 'r') as file:
#     text = file.read()
#     print(text)

os.system('pause')