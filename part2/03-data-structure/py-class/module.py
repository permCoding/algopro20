class Point():
    d = {
        'n': (0, 1),
        'ne': (1, 1),
        'e': (1, 0),
        'se': (1, -1),
        's': (0, -1)
    }

    def __init__(self, tpl):
        self.x = tpl[0]
        self.y = tpl[1]
    
    def __str__(self):
        return f'x = {self.x}; y = {self.y}'
    
    def move(self, direct, speed=1):
        self.x += self.d[direct][0]*speed
        self.y += self.d[direct][1]*speed


def get_lines(name_file, title=0):
	'''
	считать непустые строки из файла
	пропустить title строк вначале
	вернуть остальные списком
	'''
	with open(name_file, 'r') as f:
		lines = f.read().split('\n')[title:]
		return [line for line in lines if len(line)>0]
