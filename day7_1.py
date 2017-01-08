n = int(input().strip())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

Xs = sorted(X)
Ys = sorted(Y)

rx = [(Xs.index(k)+1) for k in X]
ry = [(Ys.index(l)+1) for l in Y]

sum = sum([ (rx[i] - ry[i]) ** 2 for i in range(n)])

r = 1- 6*sum / (n * ( n**2 -1 ))

print(round(r,3))
