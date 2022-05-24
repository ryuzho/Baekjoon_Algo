import sys
import collections
input = sys.stdin.readline

temp, sol = [], []
S = list(map(str, input().rstrip()))
S.append(" ")
queue = collections.deque(S)

while queue:

    c = queue.popleft()

    if c == ' ':
        while temp:
            sol.append(temp.pop())
        sol.append(" ")

    elif c == '<':

        while temp:
            sol.append(temp.pop())

        sol.append(c)
        while True:
            e = queue.popleft()
            sol.append(e)
            if e == '>':
                break
    else:
        temp.append(c)

print("".join(sol))