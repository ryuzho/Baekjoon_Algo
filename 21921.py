# 블로그

import sys
input = sys.stdin.readline

N, X = map(int, input().split())
visitors = list(map(int, input().split()))

sum_ = sum(visitors[:X])
tmp = sum_
cnt = 1

for i in range(N-X):
    tmp = tmp - visitors[i] + visitors[X+i]
    if tmp > sum_:
        sum_ = tmp
        cnt = 1
    elif tmp == sum_:
        cnt += 1


if sum_ == 0:
    print("SAD")
else:
    print(sum_)
    print(cnt)