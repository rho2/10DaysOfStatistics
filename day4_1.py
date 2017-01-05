def fact(n):
    if(n==0):
        return 1
    else:
        return n*fact(n-1)

def b(k, n, p):
    return (fact(n) / (fact(k) * fact(n-k))) * p**k * (1-p)**(n-k)

p, n = list(map(int, input().split()))
print(round(sum([b(i, n, p/100) for i in range(3)]), 3))
print(round(sum([b(i, n, p/100) for i in range(2, n+1)]), 3))
