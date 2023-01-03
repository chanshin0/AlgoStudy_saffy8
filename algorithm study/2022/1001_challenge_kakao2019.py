# 무지의 먹방 라이브
def solution(food_times, k):
    answer = 0
    l = len(food_times)
    cycle = k//l
    rear = 0
    t1 = t2 = 0
    while t1 != cycle and not food_times.count(0):
        for i in range(l):
            food_times[i] -= 1
        # print(f't초 지난 뒤 상황 : {food_times}')
        # print(f'음식먹은 위치 : {rear - 1}')
        t1 += 1
        # print(f'{t1}')

    rest = k - l*t1
    while t2 != rest:
        rear = (rear+1)%l
        if food_times[rear-1] >= 1:
            food_times[rear-1] -= 1
        else:
            while food_times[rear-1] < 1:
                rear = (rear + 1) % l
            food_times[rear - 1] -= 1
        # print(f't초 지난 뒤 상황 : {food_times}')
        # print(f'음식먹은 위치 : {rear-1}')
        # print('................')
        t2 += 1
    if not sum(food_times):
        answer = -1
    else:
        while food_times[rear] < 1:
            rear = (rear + 1) % l
        answer = rear + 1
    return answer

food_times = [4,2,3,6,7,1,5,8]
k = 27
print(solution(food_times, k))