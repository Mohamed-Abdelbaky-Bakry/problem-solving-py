X = int(input())

if X == 0 or X < 40:
    print(40 - X)
elif X == 40 or X < 70:
    print(70 - X)
elif X == 70 or X < 90:
    print(90 - X)
else:
    print("expert")