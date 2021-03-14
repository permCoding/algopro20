
key = 9

line = 'Привед Медвед...'

lst = [ord(smb)+key for smb in line]

print(lst)

result = ''
for item in lst:
    result += chr(item)

print(result)
