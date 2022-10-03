# 1로 만들기
from collections import deque
N = int(input())
visited = [0]*(10**6+1)
visited[1] = 1
que = deque([1])
while que:
    front = que.popleft()
    for i in [front*3, front*2, front+1]:
        if i == N:
            print(visited[front])
            exit(0)
        else:
            if i <= N and not visited[i]:
                visited[i] = visited[front] + 1
                que.append(i)

print(0)    # N==1이면 필요한 연산횟수는 0
