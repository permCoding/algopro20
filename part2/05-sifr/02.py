# из строки в список кодов и обратно

line = 'Привед Медвед...'

lst = [ord(smb) for smb in line]

print(lst)

result = ''
for item in lst:
    result += chr(item)

print(result)
