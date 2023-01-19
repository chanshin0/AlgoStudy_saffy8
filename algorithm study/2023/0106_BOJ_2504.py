# 괄호의 값

chars = list(input())
stack = []

rst = 0
innerVal = 0
while chars:
    now = chars.pop()
    if now in [')', ']']:
        if not stack:
            rst += innerVal
            innerVal = 0
        stack.append(now)

    else:
        if now == '(':
            top = stack.pop()
            if top == ')':
                if innerVal:
                    innerVal *= 2
                else:
                    innerVal = 2
            else:
                stack.append(top)

        elif now == '[':
            top = stack.pop()
            if top == ']':
                if innerVal:
                    innerVal *= 3
                else:
                    innerVal = 3
            else:
                stack.append(top)
        else:
            print(0)
            exit(0)
print(rst)