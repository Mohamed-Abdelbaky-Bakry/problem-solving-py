def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    l, r = map(int, input().split())
    l -= 1  # Adjusting to 0-based indexing
    r -= 1  # Adjusting to 0-based indexing

    if l < 0 or r >= n or l > r:
        print("Invalid range")
        return

    for i in range(l, r + 1):
        print(arr[i], end=" ")
    print()  # To move to the next line after printing the range


def main():
    bk = 1
    # bk = int(input())  # Uncomment this line if multiple test cases are needed
    while bk > 0:
        solve()
        bk -= 1


if __name__ == "__main__":
    main()
