def solution(name):

    a1 = min(ord(name[0]) - ord('A'), ord('Z') - ord(name[0]) + 1)
    for i in range(1, len(name)):
        a1 += 1
        a1 += min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)
        if name[i] == 'A' and i == len(name) - 1:
            a1 -= 1

    a2 = min(ord(name[0]) - ord('A'), ord('Z') - ord(name[0]) + 1)
    for i in range(-1, -len(name), -1):
        a2 += 1
        a2 += min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)
        if name[i] == 'A' and i == -len(name) + 1:
            a2 -= 1

    a3 = min(ord(name[0]) - ord('A'), ord('Z') - ord(name[0]) + 1)
    for i in range(1, name.find('A') + 1):
        a3 += 1
        a3 += min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)
        if name[i] == 'A' and i == name.find('A'):
            a3 -= 1
    for i in range(-1, -(len(name) - name.rfind('A')) - 1, -1):
        a3 += 1
        a3 += min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)
        if name[i] == 'A' and i == -(len(name) - name.rfind('A')):
            a3 -= 1

    answer = min(a1, a2, a3)
    print(a1, a2, a3)

    return answer