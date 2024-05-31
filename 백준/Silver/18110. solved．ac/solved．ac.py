# 18110 solved.ac
# 의견 바탕 난이도 결정
# 아무 의견이 없다면 난이도 0
# 의견이 있다면 30% 절사평균
# 제외 인원 정수로 반올림
# 절사 평균 정수로 반올림
import sys
import heapq

def round_up(num):
    return int(num + 1) if num - num // 1 >= 0.5 else int(num // 1)

n = int(sys.stdin.readline())
votes = [int(sys.stdin.readline()) for i in range(n)]
heapq.heapify(votes)

if n:
    crop_range = round_up(n * 0.15)
    val = 0
    for i in range(n):
        a = heapq.heappop(votes)
        if crop_range <= i < n - crop_range:
            val += a
    if val:
        print(round_up(val / (n - crop_range * 2)))
    else:
        print(val)
else:
    print(0)