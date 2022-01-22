S = list(map(int, input()))

answer = 0
for s in S:
    if answer <= 1 or s <= 1:
        answer += s
    else:
        answer *= s
print(answer)