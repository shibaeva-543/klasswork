class Point:
	
	def __init__(self, string = '0, 0'):
		coordinates = list (map (float, string.split(',')))
		self.x = coordinates[0]
		self.y = coordinates[1]
	
	def __str__(self, x = 0, y = 0):
		x = str(self.x)
		y = str(self.y)
		return x + y
	
	def __add__(self, other):
		return Point(self.x + other.x, self.y + other.y)
		
	def __radd__(self, other):
		return Point(other.x + self.x, other.y + self.y)
	
	def __sub__(self, other):
		return Point(self.x - other.x, self.y - other.y)
		
	def __rsub__(self, other):
		return Point(other.x - self.x, other.y - self.y)
		
N = int(input())
max = 0
x1 = 0
y1 = 0
X = [0] * N
Y = [0] * N

for i in range (0, N):
	b = input()
	c = Point(b)
	X[i] = c.x
	Y[i] = c.y
	dist = (c.x ** 2 + c.y ** 2) ** 0.5
	if dist >= max:
		max = dist
	x1+=c.x
	y1+=c.y

x1/=N
y1/=N
		
print (max)
print(x1, y1)

P = 0
S = 0

for i in range (0, N):
	for g in range (i+1, N):
		for k in range (i + 2, N):
			a = (((X[i] - X[g]) ** 2 + (Y[i] - Y[g]) ** 2) ** 0.5 + ((X[k] - X[g]) ** 2 + (Y[k] - Y[g]) ** 2) ** 0.5 + ((X[i] - X[k]) ** 2 + (Y[i] - Y[k]) ** 2) ** 0.5)
			if P <= a:
				P = a
			d = (a/2 * (a - ((X[i] - X[g]) ** 2 + (Y[i] - Y[g]) ** 2) ** 0.5) * (a - ((X[k] - X[g]) ** 2 + (Y[k] - Y[g]) ** 2) ** 0.5) * (a - ((X[i] - X[k]) ** 2 + (Y[i] - Y[k]) ** 2) ** 0.5)) ** 0.5
			if S<= d:
				S = d
				
print (P)
print (S)
