r, c = map(int, input().split())
map = list()
for i in range(r):
    map.append(list(input()))

for i in range(r):
    for j in range(c):
        if map[i][j] == ".":
            map[i][j] = "D"
# 어차피 디펜스 쳤으면 붙어있지 않는 한 늑대 못들어옴
for i in range(r):
    if "W" in map[i]:
        j = map[i].index("W")
        if map[max(0, i-1)][j] == "S" or map[min(i+1, r-1)][j] == "S" or map[i][max(j-1, 0)] == "S" or map[i][min(j+1, c-1)] == "S":
            print(0)
            break
else:
	print(1)
	for i in range(r):
		print("".join(map[i]))