# https://solved.ac/profile/playdev7

# 문제 - 서로 다른 N개의 자연수의 합이 S 일때, N의 최댓값은 얼마일까?
# S 가 5 라면, 1, 4 / 2, 3 처럼 최대 2개의 수를 더할 수 있는 N을 구하는 프로그램

# 욕심쟁이 알고리즘 적용
# 알고리즘만큼 중요한 것.
# 나와 타인의 차이를 인정하고 너그러운 마음을 가지는 것.
# 서로의 다름을 존중하는 것. this is tolerance!

# Commit your way to the LORD; trust in him and he will act
# Wait for God, for I shall again praise him, my savior and my God.

s = int(input())

num = 0

result = 0

# 1과 2는 예외처리
if s <= 2:
    print(1)

else:
    while num != s:
        for i in range(1, s):
            if num + i <= s:
                num += i
                result += 1
            elif num + i > s:
                num -= i-1
                result -= 1
                if num + i == s:
                    num += i
                    result += 1
            if num == s:
                break

    print(result)