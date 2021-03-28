import module as m


file_name = 'dicts.ini' # указать файл со словарями
num_dict = 2 # выбрать словарь, нумерация человеческая от 1 ...
cap = m.CaptchaNums(file_name, num_dict)
num = int(input())
print(cap.get_image_num(num))
