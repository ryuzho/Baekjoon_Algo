# 오큰수
from collections import deque

N = int(input())
seq = list(map(int, input().split()))

sol = [-1]*N
stack = deque()

for i in range(N):
    while stack and seq[i] > stack[-1][0]:
        val, idx = stack.pop()
        sol[idx] = seq[i]
    stack.append([seq[i], i])

print(*sol)