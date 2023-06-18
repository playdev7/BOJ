# https://solved.ac/profile/playdev7

# 1978 - 소수찾기

# 문제
# N개의 수가 주어진다. 그 중 소수가 몇 개인지 찾아서 출력하라.

# 입력
# 첫 줄에 수의 개수 N이 주어진다.
# 다음 줄에 공백을 기준으로 N개의 수가 주어진다.

# 출력
# N개의 수 중 소수의 개수를 출력한다.

N = int(input())
num_lis = map(int, input().split())
cnt = 0

for i in num_lis:
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        cnt += 1

print(cnt)