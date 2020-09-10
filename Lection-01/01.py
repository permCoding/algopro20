s = "Привет медвед"
lst = s.split()
s = [x[::-1] for x in lst]
print(*s)

