# https://solved.ac/profile/playdev7
# 2023 POSTECH Programming Contest Open

# A - 모범생 포닉스

# 8시간의 휴식을 취한다.
# 하루는 24시간이다.

# 입력 - 첫 줄에는 계획의 시간이 주어진다.
# 다음 줄에는 공백을 기준으로 각 계획의 소요시간이 주어진다.

# 출력 - 소요시간을 일과 시간 단위로 공백으로 구분하여 출력

# 예시 2/ 12 12 이면 => 24+8 = 32이므로 1일 8시간. "1 8" 출력

n = int(input())
plans = list(map(int, input().split()))

result = 0

for i in plans:
    result += i

result += (n-1) * 8

print(result // 24, end = " ")
print(result % 24)