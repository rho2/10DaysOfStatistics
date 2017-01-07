n = int(input())
mu = int(input())
sdev = int(input())

per = float(input())
z = float(input())

mean = mu
sd = sdev/ n**0.5

print(mu - z*sd)
print(mu + z*sd)
