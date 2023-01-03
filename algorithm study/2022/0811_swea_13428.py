import copy

T  = int(input())
for tc in range(T):
    n = list(map(int, input()))
    # [1,2,3,4,5]
# 1990 9190 9910 9110 1910 1190
    max_n = n.copy()
    for i in range(len(max_n))[::-1]: # 0 1 2 3 4 
        if max_n[i] == max(max_n):
            max_n[0], max_n[i] = max_n[i], max_n[0] # 젤큰거 맨앞이랑 바꾸기
    
    min_n = n.copy()
    for i in range(len(min_n))[::-1]: # 0 1 2 3 4 
        if min_n[i] != 0:
            if min_n[i] == min(min_n):
                min_n[0], min_n[i] = min_n[i], min_n[0] # 젤 작은거 맨앞이랑 바꾸기
        else: #0이 들어있을때 13021
            if 
            

    print(f'#{tc+1}', end=" ")
    print( ''.join(list(map(str, min_n))), ''.join(list(map(str, max_n))))
        
