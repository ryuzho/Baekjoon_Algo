# 용액

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
start, end = 0, len(arr)-1

tmp = sys.maxsize

while start < end:
    _sum = arr[start] + arr[end]
    if abs(_sum) < tmp:
        sol1, sol2 = start, end
        tmp = abs(_sum)

    if _sum > 0:
        end -= 1

    if _sum < 0:
        start += 1

    if _sum == 0:
        break

print(arr[sol1], arr[sol2])

