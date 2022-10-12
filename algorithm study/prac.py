# 22% -틀-
# [A] DFS 함수 설정
def dfs(now, n):
    global result

    # [A-1] 가지치기 조건. 주사위 횟수 n이 result보다 클 때
    if n >= result:
        return

    # [A-2] 한칸씩 총 6칸 전진한다.
    for i in range(6):
        now += 1

        # [A-3] 종료조건. 전진하다가 100에 도달하면 멈추고 result를 비교한다.
        if now == 100:
            n += 1
            if result > n:
                result = n
            return

        # [A-4] 전진하면서 뱀이든 사다리든 나오면 타고, n+1한다.
        if portal[now]:
            dfs(portal[now], n+1)

    # [A-5] 6칸 전진했으면 n+1한다.
    if not portal[now]:
        dfs(now, n+1)


# [1] 입력값 설정
from sys import stdin
N, M = map(int, stdin.readline().split())
visited = [0]*101
portal = [0]*101
for i in '_'*(N+M):
    u, v = map(int, stdin.readline().split())
    portal[u] = v

# [2] DFS 탐색. 1번칸부터 출발
result = 100
dfs(1, 0)

print(result)