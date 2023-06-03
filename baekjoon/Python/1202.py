# https://solved.ac/profile/playdev7
# 1202 / 보석 도둑

# 배낭문제
# N개의 보석이 있고 무게 M과 가격 V가 주어진다.
# 가방 K개가 있고, 가방 하나에는 하나의 보석씩만 넣을 수 있다.
# 문제 핵심 - 가방 하나에는 하나의 보석씩만 넣을 수 있다.

# 입력
# 첫 줄에 N과 K가 주어진다.
# 이후 N줄동안 보석의 무게 M 과 가격 V 가 주어진다.
# 이후 K줄동안 적재가능 무게 C가 주어진다.

# 출력
# 훔친 보석 가격의 최대합을 출력한다.

# 풀이
# 보석을 kg당 가격이 높은 순으로 내림차순 정렬
# 적재가능무게가 큰 순으로 가방을 내림차순 정렬.
# K개의 가방동안 최대한 C에 가까운 보석을 담음

import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())

# 보석삽입 - 삽입 시점과 동시에 v를 기준으로, 동일하다면 m을 기준으로 내림차순 정렬
jewelrys = deque([])
m, v = map(int, input().strip().split())
jewelrys.append([m, v])

for _ in range(N-1):
    m, v = map(int, input().strip().split())
    if jewelrys[-1][1] < v:
        jewelrys.appendleft([m, v])
    else:
        jewelrys.append([m, v])

result = 0

# 가방 삽입 시점과 동시에 담을 수 있는 최대가치를 담음
for _ in range(K):
    k = int(input().strip())
    for i in range(len(jewelrys)):
        try:
            if k >= jewelrys[i][0]:
                result += jewelrys[i][1]
                del jewelrys[i]
                break
        except:
            pass

print(result)