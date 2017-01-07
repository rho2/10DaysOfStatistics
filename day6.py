import math

maxC = int(input())
box = int(input())

mean = int(input())
sdev = int(input())

mu = box * mean
si = math.sqrt(box) * sdev
s= 0 
for i in range(maxC+1):
    e = -1 * ((i - mu)**2)/(2*(si**2))
    p = (1/(si * math.sqrt(2 * math.pi))) * math.exp(e)
    s += p

print(round(s,4))
