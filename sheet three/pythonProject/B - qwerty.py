input_numbers = input().split()

for num in input_numbers:
    p = int(num)
    print(chr(96 + p), end='')