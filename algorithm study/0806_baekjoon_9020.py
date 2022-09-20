def isdecimal(num):
    if num == 2:
        return True
    for l in range(1, int(num)+1, 2):
        if num % 2 == 0 or num == 1:
            return False
        elif num % l == 0 and l not in [1, num]:
            return False
    return True

T = int(input())
for tc in range(T):
    j_lst = []
    answer = []
    s = int(input())
    # 입력받은 s까지의 소수를 전부 리스트로
    for j in range(int(s/2)-int(s/10+1), int(s/2)+int(s/10+1)):

        if isdecimal(j):
            j_lst.append(j)
    # 그 리스트를 반 잘라서 하나씩 꺼내서 s-k가 소수라면 answer리스트에 담음
    for k in j_lst[:int(len(j_lst)/2)+1]:
        if isdecimal(s-k) == True:
            answer.append(sorted([k, s-k]))
    # answer리스트 정렬해서 맨 뒤에꺼 꺼냄
    # (여러개일시 차이가 가장 작은 것 꺼내야하니까)
    # print(answer)
    print(answer[-1][0], answer[-1][1])