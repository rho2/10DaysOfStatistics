import math

def norm(x, m , d):
    return .5*(1 + math.erf((x - m) / (d *  math.sqrt(2))))

mean, dev = map(float, input().split())
a = float(input())
b = float(input())

print(round((1 - norm(a, mean, dev))*100 , 2))

p = norm(b, mean, dev)

print(round( (1-p) * 100, 2))
print(round( p * 100, 2 ))
