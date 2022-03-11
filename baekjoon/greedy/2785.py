N = int(input())
L = list(map(int, input().split()))

L.sort()

c_len = len(L)
answer, rest = 0, c_len - 1
for i in range(c_len):
    if L[i] >= rest: # 지금 체인을 분리해서 다 결합 가능한 경우
        answer += rest # 결합 안 된 자리 카운트
        break
    else: # 지금 체인으로는 다 결합 불가능한 경우
        rest -= (L[i] + 1) # 체인 하나가 고리들로 완전히 분해되기 때문에 결합 위치 1개 더 뺌
        answer += L[i]
print(answer)