# 오큰수
import sys
input = sys.stdin.readline

A = int(input())
arr = list(map(int, input().split()))
nums = []
stack = []
sol = [0]*A
for i, v in enumerate(arr):
    nums.append((v,i))

for num in nums:

    if not stack:
        stack.append(num)

    else:
        while True:
            if stack and num[0] > stack[-1][0]:
                v, i = stack.pop()
                sol[i] = num[0]
            else:
                stack.append(num)
                break

for i in sol:
    if i == 0:
        print("-1", end = ' ')
    else:
        print(i, end = ' ')


