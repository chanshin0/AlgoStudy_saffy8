# DSLR
from sys import stdin
input = stdin.readline
from collections import deque

def push_L(n):
    if len(str(n)) == 1:
        return n
    else:
        lst_n = list(str(n))
        rst = ''
        for i in lst_n[1:]:
            rst += i
        rst += lst_n[0]

        while rst[0] == '0':
            rst = rst[1:]

        return int(rst)

def push_R(n):
    if len(str(n)) == 1:
        return n
    else:
        lst_n = list(str(n))
        rst = lst_n[-1]
        for i in lst_n[:-1]:
            rst += i

        while rst[0] == '0':
            rst = rst[1:]

        return int(rst)

T = int(input())
for tc in range(T):
    A, B = map(int, input().split())

    # register = list(range(10000))
    visited = [[] for _ in range(10000)]

    command = ['D','S','L','R']
    que = deque([A])
    visited[A] = [-1]
    while que:
        s = que.popleft()

        if visited[B] and len(visited[B]) <= len(visited[s]):
            break

        for d in range(4):
            if d == 0:
                ds = s*2
                if ds < 10000:
                    if not visited[ds] or len(visited[ds]) > len(visited[s]) + 1:
                        visited[ds] = (visited[s] + [d])
                        que.append(ds)
                else:
                    ds %= 10000
                    if not visited[ds] or len(visited[ds]) > len(visited[s]) + 1:
                        visited[ds] = (visited[s]+[d])
                        que.append(ds)
            elif d == 1:
                ds = s-1
                if 0 <= ds:
                    if not visited[ds] or len(visited[ds]) > len(visited[s]) + 1:
                        visited[ds] = (visited[s]+[d])
                        que.append(ds)
                else:
                    ds = 9999
                    if not visited[ds] or len(visited[ds]) > len(visited[s]) + 1:
                        visited[ds] = (visited[s]+[d])
                        que.append(ds)
            elif d == 2:
                ds = push_L(s)
                if not visited[ds] or len(visited[ds]) > len(visited[s]) + 1:
                    visited[ds] = (visited[s]+[d])
                    que.append(ds)
            elif d == 3:
                ds = push_R(s)
                if not visited[ds] or len(visited[ds]) > len(visited[s]) + 1:
                    visited[ds] = (visited[s]+[d])
                    que.append(ds)

    # print(visited[B])
    for i in visited[B][1:]:
        print(command[i], end='')
    print()
