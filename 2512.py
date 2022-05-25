# 예산
N = int(input())
budget = list(map(int, input().split()))
tot = int(input())
budget = sorted(budget)

upper = budget[-1]

for i in range(len(budget)):
    if budget[i]*(len(budget)-i) < tot:
        tot -= budget[i]
    else:
        upper = tot//(len(budget)-i)
        break

print(upper)

