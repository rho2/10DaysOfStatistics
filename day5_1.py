import math

def a(x):
    return 160 + 40 * x**2

def b(y):
    return 128 + 40 * y**2

A, B = map(float, input().split())

def poisson(l, k):
    return (l**k * math.exp(-1 * l)) / math.factorial(k)

def cost(rate, f):
    avg = 0
    for repairs in range(11):
        avg += poisson(rate, repairs) * f(repairs) 
    return avg

print(round(cost(A,a), 3))
print(round(cost(B,b), 3))
