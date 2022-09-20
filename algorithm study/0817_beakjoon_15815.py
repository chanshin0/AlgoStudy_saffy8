# 천재 수학자 성필
P = list(input())
stack = []
for i in range(len(P)):
    if P[i] == '+':
        a = stack.pop()
        b = stack.pop()
        stack.append(b+a)
    elif P[i] == '-':
        a = stack.pop()
        b = stack.pop()
        stack.append(b - a)
    elif P[i] == '*':
        a = stack.pop()
        b = stack.pop()
        stack.append(b * a)
    elif P[i] == '/':
        a = stack.pop()
        b = stack.pop()
        stack.append(b // a)
    else:
        stack.append(int(P[i]))

print(*stack)