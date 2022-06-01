# 블로그 solution_2

import sys
input = sys.stdin.readline
N, X = map(int, input().split())
visitors = list(map(int, input().split()))

if max(visitors) == 0:
    print("SAD")

else:
    window = sum(visitors[:X])
    max_visit = window
    cnt = 1

    for i in range(X,N):
        window = window + visitors[i] - visitors[i-X]
        if window > max_visit:
            max_visit = window
            cnt = 1
        elif window == max_visit:
            cnt += 1

    print(max_visit)
    print(cnt)



