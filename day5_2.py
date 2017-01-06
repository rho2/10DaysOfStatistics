import math

def norm(x, m , d):
    return .5*(1 + math.erf((x - m) / (d *  math.sqrt(2))))

mean, dev = map(float, input().split())
a = float(input())
b, c = map(float, input().split())

print(round(norm(a, mean, dev), 3))
print(round( norm(c, mean, dev) - norm(b, mean, dev), 3))
