m,n,a = map(int,input().split())
width = m // a
height = n // a

width += 1 if m % a > 0 else 0
height += 1 if n % a > 0 else 0

print(width * height)
