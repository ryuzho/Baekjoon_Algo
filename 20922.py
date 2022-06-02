# 겹치는 건 싫어

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

cnt = [0]*(max(arr)+1)

start, end = 0, 0
max_len = 0

while end < N:

    if cnt[arr[end]] < K:
        cnt[arr[end]] += 1
        end += 1
    else:
        cnt[arr[start]] -= 1
        start += 1

    max_len = max(max_len, end-start)

print(max_len)

