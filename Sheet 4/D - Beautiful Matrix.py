x = None
for i in range(1, 6):
    row = input().strip().split()
    for j in range(1, 6):
        num = int(row[j - 1])
        if num == 1:
            x = abs(i - 3) + abs(j - 3)

if x is not None:
    print(x)