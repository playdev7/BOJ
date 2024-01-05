# https://solved.ac/profile/playdev7

n = int(input())
board = [[0 for _ in range(101)] for _ in range(101)]
result = 0

for _ in range(n):
    x, y = map(int, input().split())
    
    for j in range(y, y+10):
        for i in range(x, x+10):
            board[j][i] += 1

dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]

for j in range(101):
    for i in range(101):
        if board[j][i] != 0:
            result += [board[j+dy[idx]][i+dx[idx]] for idx in range(4)].count(0)
            
print(result)