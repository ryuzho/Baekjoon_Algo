# 문자열 집합
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cnt = 0
S = dict()

for _ in range(N):
    S[input().rstrip()] = 1
for _ in range(M):
    word = (input().rstrip())
    if word in S:
        cnt += 1

print(cnt)