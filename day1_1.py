import statistics as st

n = int(input())
X = list(map(int, input().split()))
F = list(map(int, input().split()))
S= []

for i in range(n):
    S.extend([X[i]] * F[i])
S.sort()

su = sum(F)
if su % 2 == 0: 
    lh = S[: int(su / 2)] 
    hh = S[int(su / 2): ]
else :
    lh = S[: int((su + 1) / 2 - 1)] 
    hh = S[int((su + 1) / 2): ]

q1 = st.median(lh) 
q3 = st.median(hh)

print(round((q3 - q1) * 1.0, 1))
