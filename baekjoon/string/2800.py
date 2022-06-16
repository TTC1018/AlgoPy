import sys
input = sys.stdin.readline

S = input().rstrip()
s_len = len(S)
answer = set()

modi = {S}
while modi:
    stack = []
    nxt = set()
    for m in modi:
        for i in range(len(m)):
            if m[i] == '(':
                stack.append(i)
            elif m[i] == ')':
                if stack:
                    start = stack.pop()
                    removed = m[:start] + m[start + 1:i] + m[i + 1:] # 괄호 제거된 식
                    nxt.add(removed)
                    answer.add(removed)
    modi = nxt

answer = list(answer)
answer.sort()
for a in answer:
    print(a)