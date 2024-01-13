# https://solved.ac/profile/playdev7
# 1294 - 문자열 장식
# 주어지는 n개의 단어들을 적절히 쪼개어 사전순으로 제일 앞서는 단어 생성
# 단 쪼갠 단어는 순열이어야 함
import sys
from collections import deque

# 분할정복
def dc(idx, stack) :
    if idx == 0 :
        return ''
    if idx == 1 :
        return stack[0]

    mid = idx // 2
    left = dc(mid, stack[:mid])
    right = dc(idx - mid, stack[mid:])
    result = ''

    while left or right :
        if len(left) < len(right) :
            left, right = right, left
        if not right:
            result += left
            break
        if not left:
            result += right
            break
        if right < left[:len(right)] :
            result += right[0]
            right = right[1:]
        else :
            result += left[0]
            left = left[1:]

    return result
            
n = int(input())
print(dc(n, [sys.stdin.readline().strip() for _ in range(n)]))