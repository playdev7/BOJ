n = input()

for i in range(1, len(n)):
    a, b = n[:i], n[i:]
    x = 1
    y = 1
    for j in a:
        x *= int(j)
    for j in b:
        y *= int(j)
    if x == y:
        print("YES")
        exit()
else:
    print("NO")