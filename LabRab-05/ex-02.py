def get_for(num):
    sum = 0
    for i in range(num+1):
        sum += i
    return sum
    

def get_rec(num):
    if num == 0:
        return 0
    else:
        return get_rec(num-1) + num


n = 100
print(get_for(n))
print(get_rec(n))



# print(list(range(10)))
