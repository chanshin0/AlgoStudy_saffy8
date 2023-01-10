# 미팅 주선하기
T = int(input())
for tc in range(1, T+1):
    prefer = [[0,0,0,0,0],[6,7,8,9,10]]
    for _ in range(9):
        prefer.append(list(map(int, input().split())))

    # 인덱스:남자, ele:여자
    couples = [0]*11

    # 여자 한명씩 나와서 고백하기
    que = [6,7,8,9,10]
    cnt = 0

    while que:
        girl = que.pop(0)               # 이번에 고백할 girl

        for boy in prefer[girl]:        # girl의 선호도 순서대로 고백시도

            # [조건 1]. 남자가 짝이 없으면 짝이 된다.
            if not couples[boy]:
                couples[boy] = girl
                break
            else:
                # [조건 2]. 짝이 있으면 선호도 우선순위 높은 애를 저장, 퇴짜 맞은 애는 다시 append.
                if prefer[boy].index(couples[boy]) > prefer[boy].index(girl):
                    que.append(couples[boy])
                    couples[boy] = girl
                    break

                # [조건 3]. 태현이의 짝이 6번이 아니면서, 이번에 6번인 아닌 여자가 태현이에게 고백을 한다면
                # 태현이 선호도 순서를 바꿔서 우선순위를 높일 수 있다.
                if boy == 1 and girl != 6:
                    cnt += 1

    if couples[1] == 6:
        print('NO')
    else:
        if cnt > 1:
            print('YES')
        else:
            print('NO')
'''
1
8 7 6 10 9
7 8 10 9 6
6 7 9 8 10
7 9 8 6 10
5 1 3 2 4
3 1 4 5 2
1 3 5 4 2
2 4 3 1 5
1 2 3 5 4
'''