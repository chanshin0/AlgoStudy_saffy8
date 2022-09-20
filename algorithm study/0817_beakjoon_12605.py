#단어 뒤집기
N = int(input())
for tc in range(N):
    chars = input().split()
    print(f'Case #{tc+1}:', end=' ')
    print(' '.join(chars[::-1]))