A,B = map(int , input().split())
summ = A + B
minuss = A - B
mult = A*B
if summ >= minuss and summ >= mult:
    print(summ)
elif minuss>=summ and minuss >= mult:
    print(minuss)
else:print(mult)