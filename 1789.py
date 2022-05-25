# 수들의 합

S = int(input())

N = 0
for i in range(1, S//2+1):
    if i < S - i:
        N += 1
        S -= i
    else:
        break

print(N+1)

