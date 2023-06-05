# https://solved.ac/profile/playdev7
# 10026 - 적록색약

# 문제
# 정방행렬에 R, G, B 구역이 나뉘어져 있다.
# 적록색약은 R+G와 B구역만 구분할 수 있다.

# 입력
# 첫 째 줄에 N이 주어진다.
# 이후 N개의 줄에 N개의 값들이 주어진다.

# 출력
# 적록색약이 아닌사람이 본 구역과 적록색약인 사람이 본 구역을 공백으로 나누어 출력.

# 풀이
# BFS로 한 번 발라내고 DFS 로 계산한다.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


N = int(input().strip())

red = [[0] * N for _ in range(N)]
green = [[0] * N for _ in range(N)]
rplusg = [[0] * N for _ in range(N)]
blue = [[0] * N for _ in range(N)]

# BFS - 그리드 입력 받음과 동시에 색깔 구역 구분.
grid = list()
for i in range(N):
    m = list()
    row = input().strip()
    for j in range(N):
        m.append(row[j])
        if row[j] == "R":
            red[i][j] = 1
            rplusg[i][j] = 1
        elif row[j] == "G":
            green[i][j] = 1
            rplusg[i][j] = 1
        elif row[j] == "B":
            blue[i][j] = 1
    grid.append(m)



# 재귀를 통해 각 색상별 군집화 확인.
island = list()

def DFS(matrix, row, N):
    land = list()
    # print(f"start: {row}")

    for i in range(row, N):
        for j in range(N):
            if matrix[i][j] == 1:
                matrix[i][j] = "v"
                land.append([i, j])
                # print(i, j)
                
                try:
                    if matrix[i+1][j] == 0 and matrix[i][j+1] == 0 and matrix[i+1][0] == 0:
                        # print("진입")
                        row = i
                        stop_cnt = 0
                        for i in range(row, N):
                            if stop_cnt > 0:
                                break
                            for j in range(N):
                                if matrix[i][j] == 1:
                                    row = i
                                    stop_cnt = 1
                                    break
                        DFS(matrix, row, N)
                except:
                    pass
    
    if len(land) > 0:
        island.append(land)
        # print(land)

    return len(island)


# 정답
red_ = DFS(red, 0, N)
island = list()
blue_ = DFS(blue, 0, N)
island = list()
green_ = DFS(green, 0, N)
island = list()
rplusg_ = DFS(rplusg, 0, N)

rgb = red_ + blue_ + green_
rg_b = rplusg_ + blue_

print(rgb, rg_b)


# print(*blue, sep = "\n")
# print(*red, sep = "\n")


"""
5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
"""