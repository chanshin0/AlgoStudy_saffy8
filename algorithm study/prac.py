a = "<<<><"

def soulution(p):
    l = len(p)
    answer = 0
    for i in range(l):
        left = i
        right = l-i
        l_cnt = 0
        r_cnt = 0
        for l in range(i, -1, -1):
            if p[l]=='<':
                l_cnt += 1
                if left-l_cnt < 0:
                    answer += 1
                    break
            else:
                break

        for r in range(i,l):
            if p[r]=='>':
                r_cnt += 1
                if right-r_cnt < 0:
                    answer += 1
                    break
            else:
                break
    print(answer)
    return answer
soulution(a)