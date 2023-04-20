from itertools import combinations_with_replacement

keys = input()
password = input()

answer = 0

l = len(password)
for i in range(1, l+1):
    cb = list(combinations_with_replacement(keys, i))
    # print(len(cb))
    if (i<l):
        answer += len(cb)
    else:
        for item in cb:
            temp = ''.join(item)
            # print(temp)
            answer += 1
            if (temp==password):
                break

print(answer%900528)