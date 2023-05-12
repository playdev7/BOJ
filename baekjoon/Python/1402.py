# https://solved.ac/profile/playdev7

# 문제 a의 "정수인" 약수를 더해서 b로 만들 수 있으면 "yes"를 출력하는 프로그램.
# 정답 - 뭘 해도 yes가 나옴..
# 2에서 4 -> 2*1*1 -> 2+1+1 = 4
# 11에서 0 -> 11*-1*-1*-1*-1*-1*-1*-1*-1*-1*-1*-1* +1*-1 -> 11-1-1-1-1-1-1-1-1-1-1-1 +1-1 == 11-12+1 -> 0
# 따라서 테스트 케이스만큼 입력 받고 전부 yes 출력

test_case = int(input())

result = []

for i in range(test_case):
    a, b = map(int, input().split())
    result.append("yes")

for i in result:
    print(i)