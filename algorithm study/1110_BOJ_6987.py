# 월드컵

score_board = [list(map(int, input().split())) for _ in range(4)]
# print(score_board)

for sample in score_board:
    # 1. 승무패 합은 30
    if sum(sample) != 30:
        print(0)
        continue
    else:
        # 2. 한팀의 승무패 합은 5여야 함
        flag = 1
        for i in range(0, 18, 3):
            team_total = sum(sample[i:i+3])
            if team_total != 5:
                flag = 0
                break

        win_sum = 0
        tie_sum = 0
        tie_team = 0
        # 3. 무는 짝수, 무승부한 팀도 짝수
        for i in range(1, 18, 3):
            if sample[i] > 0:
                tie_sum += sample[i]
                tie_team += 1
            win_sum += sample[i-1]
        if (tie_sum+tie_team)%2:
            flag = 0
        # 4. (전체 경기-무승부경기)/2 = 승리(패배)경기
        if (30-tie_sum)//2 != win_sum:
            flag = 0

            
    print(flag)

'''
5 0 0 3 0 2 2 0 3 0 0 5 4 0 1 1 0 4
4 1 0 3 0 2 4 1 0 1 1 3 0 0 5 1 1 3
5 0 0 4 0 1 2 2 1 2 0 3 1 0 4 0 0 5
5 0 0 3 1 1 2 1 2 2 0 3 0 0 5 1 0 4
'''