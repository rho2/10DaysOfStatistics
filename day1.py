import math

def split(L):
    l = len(L) 
    m = l // 2
    if l % 2  == 0:
        return(L[0:m], (L[m-1]+L[m])//2, L[m:l])
    else:
        return(L[0:m], L[m], L[m+1:l])

m=int(input())
X=list(map(int, input().split()))
X.sort()

L,med,U = split(X)
_,q1,_ = split(L)
_,q3,_ = split(U)

print(q1)
print(med)
print(q3)
