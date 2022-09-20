# 개미
N1, N2 = map(int, input().split())
ant1 = list(input())[::-1]
ant2 = list(input())
T = int(input())
ant_jump = ant1+ant2       # 0초의 상태 리스트 저장


while T != 0:              # T가 0이 되면 종료
    # 1. ant1을 기준으로 비교하기 위해서 ant1의 인덱스를 구해서 리스트 저장
    ant_idx = []
    for i in range(N1+N2):
        if ant_jump[i] in ant1:
            ant_idx.append(i)

    # 2. 그 인덱스를 가지고 앞에 ant2가 있는지 확인함
    for i in ant_idx: # 0 1 2
        try:
            # 2-1. ant1앞에 ant2면 점프
            if ant_jump[i+1] in ant2:
                ant_jump[i], ant_jump[i+1] = ant_jump[i+1], ant_jump[i]
        except IndexError:
            # 2-2. 인덱스에러나면 ant1뒤에 ant2면 점프
            if ant_jump[i-1] in ant2:
                ant_jump[i-1], ant_jump[i] = ant_jump[i], ant_jump[i-1]
    T -= 1
print(''.join(ant_jump))