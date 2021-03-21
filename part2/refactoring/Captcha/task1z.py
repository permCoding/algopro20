import module as m


file_name = 'dicts.ini'
num_dict = 1 # тут нумерация человеческая от 1 ...
cap = m.CaptchaNums(file_name, num_dict)
num = int(input())
print(cap.get_image_num(num))
