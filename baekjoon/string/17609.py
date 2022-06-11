from sys import stdin

T = int(stdin.readline().rstrip())
for _ in range(T):
    s = stdin.readline().rstrip()
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] == s[right]: # 양쪽 끝 문자가 같으면 continue
            left += 1
            right -= 1
        else:
            if left < right - 1: # 우측 문자를 없애보기
                s_cpy = s[:right] + s[right + 1:]
                if s_cpy == s_cpy[::-1]: # 뒤집어도 같다면 팰린드롬
                    print(1)
                    break
            if left + 1 < right: # 좌측 문자를 없애보기
                s_cpy = s[:left] + s[left + 1:]
                if s_cpy == s_cpy[::-1]:
                    print(1)
                    break
            print(2)
            break
    else:
        print(0)