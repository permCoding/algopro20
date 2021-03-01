# словарь

def ex_1():
    numbers = [12, 100, 50, 666]

    for index, value in enumerate(numbers):
        print(index, value)


def ex_2():
    numbers = [12, 100, 50, 666]
    names = ['дюжина', 'сотня', 'полсотни', 'дьявол']
    pairs = list(zip(names, numbers))

    print(pairs)
    
    for pair in pairs:
        print(pair[0], pair[1])

ex_1()
ex_2()
