n = int(input())
result = 0
board = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(n):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    for j in range(y, y+10):
        for i in range(x, x+10):
            board[j][i] = 1

for row in board:
    result += row.count(1)

print(result)