n = int(input())
X = list(map(int, input().split()))

mean = sum(X) / n
a = sum([((x - mean) ** 2) for x in X]) / n
b = a ** 0.5

print(round(b, 1))
