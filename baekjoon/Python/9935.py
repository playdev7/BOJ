# https://solved.ac/profile/playdev7

# 9935 - 문자열 폭발

# 문제
# 문자열A가 주어진다.
# 폭발 문자열이 주어지면 폭발 문자열의 각 원소에 해당하는 문자열이 A에서 지워진다.

# 출력
# 폭발 이후의 문자열 A를 출력한다.
# 남아있는 문자가 없다면 "FRULA" 를 출력한다.

import sys

A = list(sys.stdin.readline().strip())
bomb = list(sys.stdin.readline().strip())

stack = list()

if len(bomb) == 1:
    for i in range(len(A)):
        if A[i] != bomb[0]:
            stack.append(A[i])
else:
    for i in range(len(A)):
        stack.append(A[i])
        if stack[-1] == bomb[-1] and stack[-len(bomb):] == bomb:
            for _ in range(len(bomb)):
                stack.pop()

# 삼항연산 - 스택이 있으면 출력, 비어있으면 "FRULA"
print(''.join(stack)) if stack else print("FRULA")