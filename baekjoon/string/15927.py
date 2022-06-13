import sys
input = sys.stdin.readline

s = input().rstrip()
s_len = len(s)
left, right = 0, s_len - 1
while left < right:
    if s[left] != s[right]:
        break
    else:
        left += 1
        right -= 1
else: # 팰린드롬임
    if s.count(s[0]) == s_len: # 다 똑같은 문자
        print(-1)
    else:
        print(s_len - 1)
    sys.exit()

# 팰린드롬 아님
print(s_len)