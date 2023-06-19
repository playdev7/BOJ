# https://solved.ac/profile/playdev7
# 11720 - 숫자의 합

# 문제 - N개의 숫자가 문자열로 주어졌을 때, 그 숫자들의 합을 출력하는 프로그램.
# 입력 - 숫자의 개수 n 과 길이가 n인 문자열이 주어진다.
# 출력 - 각 문자열의 수들을 더해서 출력하면 된다.

# 풀이 시작

n = int(input())
string = input()
result = 0

for i in range(n):
    result += int(string[i])

print(result)