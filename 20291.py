# 파일 정리
import sys
input = sys.stdin.readline

N = int(input())
file = dict()
for _ in range(N):
    ex = input().split('.')[1]
    if ex not in file:
        file[ex] = 1
    else:
        file[ex] += 1

sort_file = sorted(file.items())
for key,value in sorted(sort_file):
    print(f"{key.rstrip()} {value}")

