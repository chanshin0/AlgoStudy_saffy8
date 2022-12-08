# 거짓말

N, M = map(int, input().split())
cops = list(map(int, input().split()))[1:]
know_truth = [0]*51

if not cops:
    print(M)

# 경찰이 있는 파티는 제외
else:
    parties = []
    for _ in range(M):
        guests = list(map(int, input().split()))[1:]

        flag = 0
        for cop in cops:
            if cop in guests:
                flag = 1
                break
        if flag:
            for guest in guests:
                if not know_truth[guest]:
                    know_truth[guest] = 1
        else:
            parties.append(guests)

# [[7], [8], [7, 8], [9], [10]]
# [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# 한번 거짓말 들은 사람이 있는 파티도 제외
parties.sort(key=lambda x:len(x))
print(parties)
cnt = 0
while parties:
    party = parties.pop(0)
    flag = 0
    for p in party:
        if know_truth[p]:
            flag = 1
            break
        else:
            know_truth[p] = 1
    if not flag:
        cnt += 1
print(cnt)


