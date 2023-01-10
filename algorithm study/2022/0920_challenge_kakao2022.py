# 양과 늑대
from sys import stdin
def solution(info, edges):



info = [0,1,0,1,1,0,1,0,0,1,0]
edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]
visited = [0]*17
node = [[] for _ in range(len(info))]
for i, j in edges:
    node[i].append(j)
# [[1, 8], [2, 4], [], [], [3, 6], [], [5], [], [7, 9], [10, 11], [], []]


print(solution(info, edges))




