n,k = map(int,input().split())

i=0
while i<k:
    n = n // 10 if n % 10 == 0 else n - 1
    i+=1
print(n)