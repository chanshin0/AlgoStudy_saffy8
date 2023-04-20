keys = input()
password = input()

answer = 1
l = len(password)
num_keys = len(keys)

for i, char in enumerate(password):
    position = keys.index(char)
    answer += position * (num_keys ** (l - 1 - i))

answer += sum((num_keys ** i - 1) // (num_keys - 1) for i in range(1, l))

print(answer)
