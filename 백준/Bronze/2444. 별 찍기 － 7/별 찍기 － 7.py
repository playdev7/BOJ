inp = int(input())
[print(' ' * abs(inp - n) + '*' * (2 * min(n, 2 * inp - n) - 1)) for n in range(1 , 2 * inp)]