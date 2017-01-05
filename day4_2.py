a = list(map(int, input().split()))
k = int(input())
p = a[0]/a[1]

print(round((1-p)**(k - 1) * p, 3))
