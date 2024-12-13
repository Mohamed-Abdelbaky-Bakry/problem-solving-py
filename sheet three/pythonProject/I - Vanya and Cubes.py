n = int(input())
x = 0
level = 0
sum_levels = 0

while x <= n:
    level += 1
    sum_levels += level
    x += sum_levels

print(level - 1)