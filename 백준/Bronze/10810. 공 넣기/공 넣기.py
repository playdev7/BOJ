# https://solved.ac/profile/playdev7
# 10810 - 공넣기

# 문제
# 1번부터 N번까지의 N개의 바구니가 있다
# M개의 회차동안 i번 바구니부터 j번 바구니까지 k번 공을 넣으려고 한다.
# 다 넣고 나서 각 바구니에 있는 공의 번호를 순차대로 출력하라.

# 입력
# N과 M이 공백을 두고 주어진다.
# 이후 M개의 줄동안 i j k 가 공백을 두고 주어진다.

N, M = map(int, input().split())
bags = [0 for _ in range(N)]

for _ in range(M):
    i, j, k = map(int, input().split())
    for i in range(i-1, j):
        bags[i] = k

print(*bags)