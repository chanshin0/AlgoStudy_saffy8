n = int(input())
s = list(map(int, input().split()))
if n == len(s):
    a = list(map(str, s[-1::-1]))
    print(' '.join(a))

else:
    print('출석 부른 횟수를 정확히 입력해주세요')