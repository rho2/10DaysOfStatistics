def fact(n):
    if(n==0):
        return 1
    else:
        return n*fact(n-1)

def b(k, n, p):
    return (fact(n) / (fact(k) * fact(n-k))) * p**k * (1-p)**(n-k)

r, a = list(map(float, input().split()))
p = r / a

bi = sum([b(i, 6, p / (1 + p)) for i in range(3, 7)])

print(round(bi, 3))
