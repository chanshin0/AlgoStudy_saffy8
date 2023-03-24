# 쿼드트리

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
print(arr)
answer = ()
depth = 1
quad_1 = [(0,0), (N//2**(depth)-1, (N//2**(depth))-1)]
quad_2 = [(0,(N//2**(depth))), ((N//2**(depth)-1), N)]
quad_3 = [((N//2**(depth)),0), (N, (N//2**(depth)))]
quad_4 = []
