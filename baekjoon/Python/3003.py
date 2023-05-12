default = 1, 1, 2, 2, 2, 8
hyeok  = list(map(int, input().split()))

for i in range(6):
	print(default[i]-hyeok[i], end=' ')
