import sys
input = sys.stdin.readline

S = list(input().rstrip())

word = ''
sol = ''
flag = False

for i in S:
    if flag == False:
        if i == '<':
            flag = True
            word += i
        elif i == ' ':
            word += i
            sol += word
            word = ''
        else:
            word = i+word

    elif flag == True:
        word += i
        if i == '>':
            flag = False
            sol += word
            word = ''

print(sol+word)