n = int(input())
x = list(map(int, input().split()))
w = list(map(int, input().split()))

m = sum([x[i]*w[i] for i in range(n)])
s = sum(w)
print(round(m/s,1 ))
