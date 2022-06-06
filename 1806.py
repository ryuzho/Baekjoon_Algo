# 부분 합
import sys
input = sys.stdin.readline
N, S = map(int, input().split())
arr = list(map(int, input().split()))
arr.append(0)
left, right = 0, 0
flag, sum_ = 0, 0
sol = float("INF")

while right <= N:

    if sum_ < S:
        sum_ += arr[right]
        right += 1
    if sum_ >= S:

        flag = 1
        tmp = right-left
        if sol > tmp:
            sol = tmp

        sum_ -= arr[left]
        left += 1


if flag == 1:
    print(sol)
else:
    print("0")
