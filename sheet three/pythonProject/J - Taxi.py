import math

n = int(input())
cn1 = cn2 = cn3 = cnc = 0

groups = list(map(int, input().split()))

for s in groups:
    if s == 1:
        cn1 += 1
    elif s == 2:
        cn2 += 1
    elif s == 3:
        cn3 += 1
    elif s == 4:
        cnc += 1

cnc += cn3
if cn3 >= cn1:
    cn1 = 0
else:
    cn1 -= cn3

cnc += cn2 // 2
if cn2 % 2 == 0:
    cn2 = 0
else:
    cn2 = 1

if cn2 == 1:
    cnc += 1
    cn1 -= 2

if cn1 > 0:
    cnc += math.ceil(cn1 / 4.0)

print(cnc)