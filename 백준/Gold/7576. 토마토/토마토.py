# https://solved.ac/profile/playdev7

# 7576 - 토마토
# N행 M열의 토마토 박스에 대한 탐색 문제.

# 입력
# 첫줄에 M과 N이 주어진다. - 열과 행이 주어진다.
# 이후 N개의 줄동안 N * M 의 행렬이 주어진다.
# 각 값의 의미는 아래와 같다.
	# -1은 토마토가 없는 것
	# 0은 익지 않은 토마토
	# 1은 이미 익은 토마토

# 모든 토마토가 익는 최소 날짜를 출력한다.
# 처음부터 익은 상태면 0을 출력한다
# 모두 익힐 수 없는 상태라면 -1을 출력한다.

# 풀이
# 익은 토마토의 인덱스를 구한다.
# 이후 해당 인덱스를 기준으로 상하좌우를 탐색하고 1씩 부여한다.

import sys
from collections import deque

col, row = map(int, sys.stdin.readline().strip().split())
tomatos = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(row)]
ans = 0

# 사분면 - 좌우상하
dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]


# deque 를 통한 탐색
queue = deque()

# 이미 익은 토마토의 좌표 구하기
for x in range(row):
    for y in range(col):
        if tomatos[x][y] == 1:
            queue.append([x, y])

# BFS를 통해 방문 할 때마다 값을 1씩 더해줌
while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if -1 < nx < row and -1 < ny < col and tomatos[nx][ny] == 0:
            tomatos[nx][ny] = tomatos[x][y] + 1
            queue.append([nx, ny])

for tomato in tomatos:
    for toma in tomato:
        if toma == 0:
            print(-1)
            exit()
        elif ans < toma:
            ans = toma

# 방문 당시부터 1이 더 더해졌으므로 1을 감산.
print(ans - 1)