P, S = input().strip(), input().strip()


def get_table(x): # 접두사와 접미사가 일치하는 길이를 기록
    arr = [0 for _ in range(len(x))]
    j = 0
    for i in range(1, len(x)):
        while j > 0 and x[i] != x[j]:
            j = arr[j - 1]
        if x[i] == x[j]:
            j += 1
            arr[i] = j
    return arr


def kmp(word, find):
    result = 0
    j = 0
    for i in range(len(word)):
        while j > 0 and word[i] != find[j]:
            j = table[j - 1]
        if word[i] == find[j]:
            if j == len(find) - 1:
                result += 1
                j = table[j]
            else:
                j += 1
    return result


table = get_table(S)
result = kmp(P, S)
print(1 if result else 0)