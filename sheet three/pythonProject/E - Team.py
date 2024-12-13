
n = int(input())

ans = 0
i = 0
while i < n:
    a, b, c = map(int, input().split())

    if (a + b + c) >= 2:
        ans += 1

    i += 1

print(ans)