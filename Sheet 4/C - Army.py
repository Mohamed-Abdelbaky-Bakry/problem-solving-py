n = int(input())
arr = list(map(int, input().split()))
a, b = map(int, input().split())
total_sum = sum(arr[a-1:b-1])
print(total_sum)