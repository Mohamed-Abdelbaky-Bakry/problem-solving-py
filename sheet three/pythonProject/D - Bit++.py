n = int(input())
x = 0
i = 0
while i < n:
    str_op = input()
    if str_op == "X++" or str_op == "++X":
        x += 1
    else:
        x -= 1
    i += 1
print(x)