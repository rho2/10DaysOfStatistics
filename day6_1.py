import math

ti = int(input())
stu = int(input())

mean = float(input())
sdev = float(input())

mean = mean * stu
sdev = sdev * math.sqrt(stu)

p = (1/2)*(1 + math.erf((ti-mean)/(2**(1/2)*sdev)))
    
print(round(p,4))
