str = input()
target = input()
length = len(target)

answer = 0

i = 0
while i < len(str):
    if str[i:i+length] == target:
        answer += 1
        i += length
    else:
        i += 1
print(answer)
# print(str.count(target))