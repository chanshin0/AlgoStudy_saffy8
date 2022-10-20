# DSLR
from sys import stdin
input = stdin.readline
from collections import deque

T = int(input())
for tc in range(T):
    A, B = map(int, input().split())

    calculator = ['D','S','L','R']
    visited = [0]*10000
    que = deque([(A, '')])
    ans = ''
    while que:
        s, cals = que.popleft()
        visited[s] = 1

        if visited[B] and len(ans) <= len(cals):
            break

        for d in calculator:
            if d == 'D':
                ds = s*2
                if ds >= 10000:
                    ds = ds % 10000

                if 0 <= ds < 10000 and not visited[ds]:
                    visited[ds] = 1
                    que.append((ds, cals+d))
                    visited[ds] = 0

                if ds == B:
                    if len(ans) > len(cals)+1 or ans == '':
                        ans = cals+d

            elif d == 'S':
                if s == 0:
                    ds = 9999
                else:
                    ds = s-1
                if 0 <= ds < 10000 and not visited[ds]:
                    visited[ds] = 1
                    que.append((ds, cals+d))
                    visited[ds] = 0

                if ds == B:
                    if len(ans) > len(cals)+1 or ans == '':
                        ans = cals+d

            elif d == 'L':
                ds = str(s)
                while len(ds) != 4:
                    ds = '0' + ds
                ds = ds[1:] + ds[0]
                ds = int(ds)
                if 0 <= ds < 10000 and not visited[ds]:
                    visited[ds] = 1
                    que.append((ds, cals+d))
                    visited[ds] = 0

                if ds == B:
                    if len(ans) > len(cals)+1 or ans == '':
                        ans = cals+d

            elif d == 'R':
                ds = str(s)
                while len(ds) != 4:
                    ds = '0' + ds
                ds = ds[-1] + ds[1:]
                ds = int(ds)
                if 0 <= ds < 10000 and not visited[ds]:
                    visited[ds] = 1
                    que.append((ds, cals+d))
                    visited[ds] = 0

                if ds == B:
                    if len(ans) > len(cals)+1 or ans == '':
                        ans = cals+d

    print(ans)



