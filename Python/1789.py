# 문제 - 서로 다른 N개의 자연수의 합이 S 일때, N의 최댓값은 얼마일까?
# S 가 5 라면, 0, 1, 4 / 0, 2, 3 처럼 최대 3개의 수를 더할 수 있는 N을 구하는 프로그램
# 욕심쟁이 알고리즘 적용 - 교수님 감사합니다.

s = int(input())

num = 0

result = 0

while num != s:
    for i in range(s):
        if num + i < s:
            num += i
            result += 1
        elif num + i > s:
            num -= i-1
            result -= 1
            if num + i == s:
                num += i
                result += 1
                break
            else:
                pass
        if num == s:
            break

print(result)