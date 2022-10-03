# 모든 순열
def perm(s, N):     # 이번에 자리정할 인덱스, 순열배열의 길이
    if s == N:
        print(*p)    # s가 N까지 왔으면 0~N-1번 자리까지 다 정했다는 의미이므로 종료

    else:
        for i in range(N):      # 모든 원소에 대해서
            if not used[i]:     # i가 사용안됐다면
                p[s] = nums[i]  # 순열에 사용하고
                used[i] = 1     # 사용처리한 후
                perm(s+1, N)    # 다음자리 정하러 보냄
                used[i] = 0     # 다음 반복문에 사용할 수 있게 초기화
N = int(input())
nums = list(range(1, N+1))
l = len(nums)
p = [0]*l
used = [0]*l
perm(0, l)
