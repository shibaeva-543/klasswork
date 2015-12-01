from decimal import Decimal, getcontext

getcontext().prec = 2

s = Decimal(input())

x = float (input())

y = int (input())

A = x / 12 * (1 + x / 12) ** (y * 12) / ((1 + x / 12) ** (y * 12) - 1)

egm = Decimal(A * float(s))

s1 = 0

print(egm)

