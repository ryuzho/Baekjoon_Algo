# 오큰수
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

for i, v in enumerate(A):
    for j in