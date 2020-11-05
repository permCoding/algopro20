a = 2
lst = [1, 2, 3, 4, 5]
n = len(lst)


new_list = lst[:n] if a%2 == 0 else lst[:n][::-1]
print(", ".join(str(e) for e in new_list))
