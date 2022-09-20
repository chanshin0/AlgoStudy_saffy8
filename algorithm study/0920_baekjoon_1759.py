# 암호 만들기
from sys import stdin
from itertools import combinations
L, C = map(int, stdin.readline().split())
chars = sorted(list(stdin.readline().split()))

vowel = ['a','e','i','o','u']
for i in combinations(chars, L):      # 갓터툴
    code = ''.join(i)
    for j in range(L-1):                 # 오름차순인지 확인
        if ord(i[j]) < ord(i[j+1]):
            if j == L-2:                    # 오름차순 확인 다 됐으면
                cnt = 0
                for v in vowel:                 # 자음모음 조건 확인
                    if v in code:
                        cnt += 1
                if 1 <= cnt <= L - 2:           # 모음은 최소 1개, 최대 L-2개
                    print(code)                 # 출력
        else:
            break                         # 오름차순 아니면 확인 그만

