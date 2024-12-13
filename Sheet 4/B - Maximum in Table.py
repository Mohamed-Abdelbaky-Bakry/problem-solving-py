def solve():
    n = int(input())
    # Create a 2D list with initial values set to 1
    arr = [[1 for _ in range(n)] for _ in range(n)]

    # Fill the DP table
    for i in range(1, n):
        for j in range(1, n):
            arr[i][j] = arr[i - 1][j] + arr[i][j - 1]

    # The result is the bottom-right corner value
    print(arr[n - 1][n - 1])


def main():
    bk = 1
    # bk = int(input())  # Uncomment if multiple test cases are needed
    while bk > 0:
        solve()
        bk -= 1


if __name__ == "__main__":
    main()
