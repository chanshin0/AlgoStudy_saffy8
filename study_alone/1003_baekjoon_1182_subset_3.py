# 부분수열의 합

# 이 방법은 비트를 쓰지 않기 때문에, 부분집합의 합을 가지고만 풀 수있는 문제는 적용가능 하지만,
# 부분 집합을 가지고 조건을 넣어야 하는 문제는 풀 수 없음. (크기가 양수인 부분집합에 대하여~)
def f(i, N, s, t):
    global answer
    global cnt
    cnt += 1
    if i == N:                          # 모든 원소가 고려된 경우
        if sum(bit):                        # 여긴데 안먹힘!
            if s == t:                      # 부분집합의 합이 t면
                answer += 1
        return
    else:
        f(i+1, N, s+nums[i], t)        # A[i]가 포함된 경우
        f(i+1, N, s, t)                # A[i]가 포함되지 않은 경우

from sys import stdin
N, S = map(int, stdin.readline().split())
nums = list(map(int, input().split()))
l = len(nums)
bit = [0]*l
answer = 0
cnt = 0
f(0, l, 0, S)
print(answer, cnt)
#