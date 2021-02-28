# словарь

def ex_1():
    pairs = {
        'дюжина': 12,
        'сотня': 100, 
        'полсотни': 50,
        'дьявол': 666
    }
    for key in pairs.keys():
        print(key, pairs[key])


def ex_2():
    numbers = [12, 100, 50, 666]
    names = ['дюжина', 'сотня', 'полсотни', 'дьявол']
    pairs = dict(zip(names, numbers))

    for key in pairs.keys():
        print(key, pairs[key])


ex_1()
ex_2()
