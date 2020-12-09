def get(x):
    return x ** 2
    
lst = [get(i) for i in range(10)]

print(lst)