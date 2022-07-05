import sys
input = sys.stdin.readline


S = input().rstrip()
answer = ''
tmp = ''
stack = False
for s in S:
    if stack:
        if s == '>':
            stack = False
        answer += s
    else:
        if s.isalnum():
            tmp += s
        else:
            answer += tmp[::-1]
            tmp = ''
            if s == '<':
                answer += s
                stack = True
            else:
                answer += s
answer += tmp[::-1]
print(answer)