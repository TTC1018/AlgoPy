import sys
input = sys.stdin.readline
open = {'(', '['}
close = {')', ']'}
oppo = {')': '(', ']': '['}
num_val = {'(': 2, '[': 3, ')': 2, ']': 3}


S = input().rstrip()
stack = []
answer, tmp_answer = 0, 1

for i in range(len(S)):
    if S[i] in open:  # 열린 괄호
        tmp_answer *= num_val[S[i]]
        stack.append(S[i])
    elif S[i] in close:  # 닫힌 괄호
        if not stack or stack[-1] != oppo[S[i]]: # 올바른 괄호쌍 아닌 경우
            print(0)
            sys.exit()

        if S[i - 1] == oppo[S[i]]: # 바로 닫히는 괄호쌍 (정산 시점)
            answer += tmp_answer

        stack.pop() # 열린 괄호 제거
        tmp_answer //= num_val[S[i]] # 곱했던 수 원상복구

if stack:
    print(0)
else:
    print(answer)
