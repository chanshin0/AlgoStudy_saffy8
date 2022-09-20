# 양과 늑대
from sys import stdin
def solution(info, edges):
    answer = 0
    sheep = 1
    wolf = 0
    queue = [0]
    while queue:
        front = queue.pop(0)
        visited[front] = 1
        for n in node[front]:
            if visited[n] == 0:
                if info[n] == 0:            # 다음 길이 양이면
                    sheep += 1
                    queue.append(n)
                    info[n] = -1
                else:                       # 다음 길이 늑대이면
                    if wolf + 1 < sheep:
                        wolf += 1
                        queue.append(n)
                    else:
                        if node[n] != []:
                            queue.append(n)

    return answer, sheep, wolf

info = [0,1,0,1,1,0,1,0,0,1,0]
edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]
visited = [0]*17
node = [[] for _ in range(len(info))]
for i, j in edges:
    node[i].append(j)
# [[1, 8], [2, 4], [], [], [3, 6], [], [5], [], [7, 9], [10, 11], [], []]


print(solution(info, edges))

전위 순회 사용해서 다시 풀어보기



