from fractions import Fraction

x0 = 4
x1 = 4.25
for i in range (2, 30):
	f=108 - Fraction((815 - Fraction(1500 / x0)) / x1)
	x1, xo = f, x1
print (f)
