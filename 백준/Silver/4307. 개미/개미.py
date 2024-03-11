# 4307 - 개미
# 풀이
# 최단거리 => 0까지의 거리, l까지의 거리 중 최소값 집합의 최대값
# 최장거리 => 집합 중 최대값
import sys

t = int(sys.stdin.readline())
for _ in range(t):
    l, n = map(int, sys.stdin.readline().split())
    min_val, max_val = int(), int()
    for i in range(n):
        x = int(sys.stdin.readline())
        min_val = max(min(x, abs(l-x)), min_val)
        max_val = max(max(x, abs(l-x)), max_val)
    print(min_val, max_val)