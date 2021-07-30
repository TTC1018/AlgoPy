from collections import deque

A, B, C = [int(n) for n in input().split(' ')]
ABC = '0:0:' + str(C)

answer = []
q = deque()
q.append(ABC)

visited = set()
while q:
    A_B_C = q.popleft()

    if A_B_C not in visited:
        visited.add(A_B_C)
        if A_B_C[0] == '0':
            answer.append(A_B_C.split(':')[-1])

        num_list = A_B_C.split(':')
        for idx, bottle in enumerate(num_list):
            if bottle != '0':
                bot_num = int(bottle)
                space_A = A - int(num_list[0])
                space_B = B - int(num_list[1])
                space_C = C - int(num_list[2])
                if idx == 0:
                    new_A = bot_num - space_B if bot_num - space_B >= 0 else 0
                    new_B = int(num_list[1]) + bot_num if int(num_list[1]) + bot_num <= B else B
                    q.append(str(new_A) + ':' + str(new_B) + ':' + num_list[2])

                    new_A2 = bot_num - space_C if bot_num - space_C >= 0 else 0
                    new_C = int(num_list[2]) + bot_num if int(num_list[2]) + bot_num <= C else C
                    q.append(str(new_A2) + ':' + num_list[1] + ':' + str(new_C))
                elif idx == 1:
                    new_B = bot_num - space_A if bot_num - space_A >= 0 else 0
                    new_A = int(num_list[0]) + bot_num if int(num_list[0]) + bot_num <= A else A
                    q.append(str(new_A) + ':' + str(new_B) + ':' + num_list[2])

                    new_B2 = bot_num - space_C if bot_num - space_C >= 0 else 0
                    new_C = int(num_list[2]) + bot_num if int(num_list[2]) + bot_num <= C else C
                    q.append(num_list[0] + ':' + str(new_B2) + ':' + str(new_C))
                elif idx == 2:
                    new_C = bot_num - space_A if bot_num - space_A >= 0 else 0
                    new_A = int(num_list[0]) + bot_num if int(num_list[0]) + bot_num <= A else A
                    q.append(str(new_A) + ':' + num_list[1] + ':' + str(new_C))

                    new_C2 = bot_num - space_B if bot_num - space_B >= 0 else 0
                    new_B = int(num_list[1]) + bot_num if int(num_list[1]) + bot_num <= B else B
                    q.append(num_list[0] + ':' + str(new_B) + ':' + str(new_C2))


answer = [int(n) for n in list(set(answer))]
answer = sorted(answer)
answer = ' '.join([str(n) for n in answer])
print(answer)