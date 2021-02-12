num_1 = int(input("Введите первое число - "))
num_2 = int(input("Введите второе число - "))


# тут нужно if`ом выбрать кто больше
num_max = num_1
num_min = num_2

if (num_max % num_min == 0):
    print(num_max, "кратно", num_min)
else:
    print("не кратно")


# print(19 / 3)
# print(19 // 3)
# print(19 % 3)
# print(19 % 2)
# print(18 % 2)
# print(18 % 2 == 0)
'''
так вычисляется остаток от целочисленного деления
19 // 3 = 6
6 * 3 = 18
19 - 18 = 1
'''



