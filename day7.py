import statistics
n = int(input())

X = list(map(float, input().split()))
Y = list(map(float, input().split()))

ux = statistics.mean(X)
uy = statistics.mean(Y)

sx = statistics.pstdev(X, ux)
sy = statistics.pstdev(Y, uy)

p = sum([(X[i]-ux)* (Y[i]-uy) for i in range(n)]) / (n * sx * sy)

print(round(p, 3))
