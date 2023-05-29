x = int(input())
files = []
f_name = list(list(input()) for _ in range(x))

for i in range(len(f_name)):
    if f_name[0] != f_name[i]:
        for j in range(len(f_name[0])):
            if f_name[0][j] != f_name[i][j]:
                f_name[0][j] = "?"

print("".join(f_name[0]))