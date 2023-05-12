# https://solved.ac/profile/playdev7
# 2745 - 진법 변환

# 숫자 A가 주어지면, B진법으로 변환하는 프로그램 작성.
# 핵심 - 10진수로 변환해야 하기 위해 n의 각 문자에 b ** i 를 곱해줘야한다. (0 제외)
# 풀이 시작.

result = 0
n, b = input().split()
b = int(b)

# 10진수로 변환해야 하기 위해 n의 각 문자에 b ** i 를 곱해줘야한다. (0 제외)
# 오른쪽에서 왼쪽으로 연산이 필요하기 때문에, 문자열 n을 뒤집어준다.
n_list = list(n)
n_list.reverse()

# 0부터 9까지의 숫자를 의마하는 문자인지 확인하기 위한 리스트도 추가로 생성한다.
nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# 0번 인덱스의 경우 대응하는 값만 더해준다.
# ASCII 상 "A" 는 65이므로 ord()  -55를 해주면 문제와 일치하다.
if n_list[0] not in nums:
    result += ord(n_list[0]) - 55
else:
    result += int(n_list[0])

for i in range(1, len(n_list)):
    if n_list[i] not in nums:
        result += (ord(n_list[i]) - 55) * (b ** i)
    else:
        result += int(n_list[i]) * (b ** i)

print(result)