n = int(input())

for i in range(1, n + 1):
    check_lucky = True
    num = i
    while num > 0:
        if num % 10 == 4 or num % 10 == 7:
            num //= 10
        else:
            check_lucky = False
            break

    if check_lucky and n % i == 0:
        print("YES")
        break
else:
    print("NO")