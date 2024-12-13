N = int(input())
ones = N % 10
hun = N // 100

print("Yes" if ones == hun else "No")