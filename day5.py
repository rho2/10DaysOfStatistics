import math
x = 5

l = float(input())
k = float(input())

p = ((l**k)*math.exp(-1*l)) / math.factorial(k)

print(round(p,3))
