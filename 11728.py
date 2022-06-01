# 배열 합치기
import sys
input = sys.stdin.readline

arr = []
N, M = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
arr = arr1+arr2
arr.sort()

for i in arr:
    print(i, end=' ')