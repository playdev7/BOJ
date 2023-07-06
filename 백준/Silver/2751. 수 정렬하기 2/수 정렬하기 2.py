# https://solved.ac/profile/playdev7

# 2751 - 수 정렬하기 2

# 문제
# N개(최대 백만개)의 정수가 주어진다. 이를 오름차순 정렬하여 출력하라.

# 입력
# N이 주어진다. 이후 N번에 거쳐 추가 입력이 주어진다.

# 출력
# 하나씩 개행하며 출력한다.

# 풀이
# heap 정렬한다.

import sys
import heapq

N = int(input())
nums = [int(sys.stdin.readline().strip()) for _ in range(N)]
heapq.heapify(nums)

while nums:
    print(heapq.heappop(nums))