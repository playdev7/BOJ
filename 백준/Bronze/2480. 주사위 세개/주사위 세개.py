# 문제 - 입력이 주어졌을 때 조건에 맞춰 상금을 출력하기
# 조건 - 입력받은 주사위 세 개의 값에 따라 다른 값을 출력 

# 공백을 기준으로 한 줄에 세 개의 눈이 주어진다.
a, b, c = map(int, input().split())

reward = 0

# 같은 눈이 3개가 나오면 10000 + 같은 눈 * 1000 원의 상금을 받는다
if a == b and b == c:
    reward = 10000 + a * 1000

# 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다. 
elif a == b or a == c or b == c:
    # a == b 또는 a == c 조합일 경우
    if a == b or a == c:
        reward = 1000 + a * 100
    # b == c 조합일 경우
    else:
        reward = 1000 + b * 100

# 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.  
else: 
    # a가 제일 클 때
    if a > b and a > c:
        reward = a * 100

    # b가 제일 클 때
    elif b > a and b > c:
        reward = b * 100

    # c가 제일 클 때
    else:
        reward = c * 100

print(reward)