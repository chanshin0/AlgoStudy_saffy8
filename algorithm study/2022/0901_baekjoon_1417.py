# 국회의원 선거
N = int(input())
vote = [0]*(N+1)
for n in range(1, N+1):
    vote[n] = int(input())

if N > 1:
    cnt = 0
    while max(vote[2:]) >= vote[1]:
        target = max(vote[2:])
        for i in range(2, N+1):
            if vote[i] == target:
                vote[i] -= 1
                vote[1] += 1
                cnt += 1
                break
    print(cnt)
else:
    print(0)
