import sys
input = sys.stdin.readline


N = int(input())
S = ''.join([input().rstrip() for _ in range(N)])

T = ''
left, right = 0, N - 1
cnt = 0
while left <= right:
    if S[left] < S[right]:
        T += S[left]
        left += 1
    elif S[left] > S[right]:
        T += S[right]
        right -= 1
    else:
        l, r = left, right
        while l <= r:
            if S[l] < S[r]:
                T += S[left]
                left += 1
                break
            elif S[l] > S[r]:
                T += S[right]
                right -= 1
                break
            l += 1
            r -= 1
        else:
            T += S[left]
            left += 1

    cnt += 1
    if not cnt % 80:
        T += '\n'
print(T)