# 이전 순열
N = int(input())
target = list(map(int, input().split()))
cnt = 0
for i in range(N-1, 0 ,-1):                 # 맨 뒤 부터
    if target[i] < target[i-1]:             # 정렬할 것 찾고
        for j in range(N-1, i-1, -1):           # 다시 맨 뒤부터 i까지
            if target[i-1] > target[j]:         # i-1번째 원소보다 더 큰게 있으면
                target[i-1], target[j] = target[j], target[i-1] # 스왑하고
                target = target[:i] + sorted(target[i:], reverse=True)        # 나머지 인덱스 정렬해서 저장
                break
        break       # 바로 다음 순열찾는 문제니까 스왑했으면 바로바로 종료
    else:
        cnt += 1
print(-1) if cnt == N-1 else print(*target)