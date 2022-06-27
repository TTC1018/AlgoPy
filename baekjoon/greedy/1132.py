from collections import defaultdict
import sys
input = sys.stdin.readline


N = int(input())
nums = [input().rstrip() for _ in range(N)]
d = defaultdict(int)

not_to_be_zero = set()
for num in nums:
    n_len = len(num)
    d[num[0]] += 10**(n_len - 1)
    not_to_be_zero.add(num[0]) # 첫번째 수가 0이 되면 안 됨

    limit = n_len
    n_len -= 1
    for i in range(1, limit):
        d[num[i]] += 10**(n_len - 1)
        n_len -= 1


d = sorted(d.items(), key=lambda x:x[1])
if len(d) == 10 and d[0][0] in not_to_be_zero: # 0써야 되는데 0이 되면 안 되는 알파벳일 때
    for i in range(1, 10):
        if d[i][0] not in not_to_be_zero:
            d.remove(d[i]) # 순서는 유지해야 되기 때문에 대체 알파벳만 없애면 됨 (0은 얼마나 많든 무조건 0)
            break

answer = 0
num_val = 9
for i in range(len(d) - 1, -1, -1):
    answer += (d[i][1] * num_val)
    num_val -= 1
print(answer)