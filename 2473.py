# 세 용액

import sys
input = sys.stdin.readline

N = int(input())
arr = sorted(list(map(int, input().split())))

tmp = sys.maxsize

for i in range(len(arr)-2):

    start, end = i+1, len(arr)-1

    while start < end:
        _sum = arr[i] + arr[start] + arr[end]
        if abs(_sum) < tmp:
            tmp = abs(_sum)
            sol1, sol2, sol3 = i, start, end

        if _sum > 0:
            end -= 1
        elif _sum < 0:
            start += 1
        else:
            break

print(arr[sol1],arr[sol2],arr[sol3])
