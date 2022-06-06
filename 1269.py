# 대칭 차집합
input()
A = set(list(map(int, input().split())))
B = set(list(map(int, input().split())))
print(len(A-B)+len(B-A))