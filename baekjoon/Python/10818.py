# https://solved.ac/profile/playdev7
# 10818 - 최소, 최대

# 문제 - n개의 정수가 입력되었을 때 최솟값과 최댓값을 공백으로 구분하여 출력하는 프로그램 작성.
# 입력 - 첫 줄에 정수의 개수 n, 다음 줄에 공백을 기준으로 n개의 숫자들이 입력된다.

# 풀이 시작

n = int(input())
num_lis = list(map(int, input().split()))

max_ = num_lis[0]
min_ = num_lis[0]

# min(), max() 대신 직접 탐색해보자.
for i in num_lis:
    if max_ < i:
        max_ = i
    if i < min_:
        min_ = i

# 이후 최솟값, 최댓값 순으로 공백을 기준으로 구분하여 출력시킨다.
print(min_, max_)