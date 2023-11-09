# https://solved.ac/profile/playdev7
# 1463 - 1로 만들기
# 직전 원소의 최소경우의 수

x = int(input())
dp = list(range(x+1))

for i in range(2, x+1):
    # 직전 원소를 땡겨옴
    dp[i] = dp[i-1] + 1
    # 2로 나누어지는 구간에서 2로 나눔
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    # 3으로 나누어지면 3으로 나눔
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[x]-1)