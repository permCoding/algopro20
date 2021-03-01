class Point():
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def __str__(self):
		# return str(self.x) + ':' + str(self.y)
		# return 'y = {1}; x = {0}'.format(self.x,self.y)
		# return 'x =%3d; y =%3d' % (self.x, self.y)
		return f'x = {self.x}; y = {self.y}'


a = Point(10,3)
b = Point(0,0)

print(int(a.x), int(a.y))
print(a)
