import statistics

n = 5
X = [95, 85, 80, 70, 60]
Y = [85, 95, 70, 65, 70]

b = (n * sum([X[i] * Y[i] for i in range(n)]) - ( sum(X) * sum(Y) )) / (n * sum([X[i] * X[i] for i in range(n)]) - sum(X) * sum(X))

a = statistics.mean(Y) - b * statistics.mean(X)

y = a + b * 80

print(round(y, 3))
