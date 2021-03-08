# формируем имена всех файлов
name_file_in = 'block.txt'
name_file_pat = 'pattern.html'
name_file_out = name_file_in.split('.')[0] + '.html'

# читаем исходный файл
file_in = open(name_file_in, encoding='utf-8')
lines_in = file_in.readlines()
file_in.close()

# читаем файл шаблона
file_pat = open(name_file_pat, encoding='utf-8')
lines_pat = file_pat.readlines()
file_pat.close()

# формируем абзацы стиха с учётом возможного разного кол-ва строк в абзаце
parags = []
for parag_lines in ''.join(lines_in[2:]).split('\n\n'): # абзац по двойному символу переноса
    parags.append('<p>' + '<br>\n'.join(parag_lines.split('\n')) + '</p>\n')

# формируем строки итогового файла
lines_for_public = []
for line in lines_pat: # читаем из шаблона
    lines_for_public.append(line) # добавляем в итоговый
    if '<title>' in line:
        lines_for_public.append(lines_in[0].strip())
    if '<body>' in line:
        lines_for_public.extend(parags)

# пишем в итоговый файл
file_out = open(name_file_out, mode='w', encoding='utf-8')
file_out.writelines(lines_for_public)
file_out.close()
