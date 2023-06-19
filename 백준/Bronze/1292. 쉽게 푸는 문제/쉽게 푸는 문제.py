# https://solved.ac/profile/playdev7
# 1292 / 쉽게 푸는 문제

# 문제
# 해당하는 수의 횟수만큼 더하는 수열이 있다. 2면 2+2 3이면 3+3
# 수열의 시작과 끝이 주어지면 해당 수열을 인덱싱해서 총합을 출력해라.
# 수열은 1부터 1000 까지이다. (1000을 포함한다.)

start, end = map(int, input().split())
result = 0
seq = list()

for i in range(1, 1001):
    for j in range(i):
        seq.append(i)

for i in range(start, end+1):
    result += seq[i-1]

print(result)