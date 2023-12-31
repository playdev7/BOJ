# https://sovled.ac/profile/playdev7
# 1009 - 분산처리

def power(a,b,m):
    result = 1
    while b > 0:
        if b % 2 != 0:
            result = (result * a) % m
        b //= 2
        a = (a * a) % m

    return result

for _ in range(int(input())):
    a, b = map(int, input().split())
    c = power(a, b, 10)
    if c == 0:
        print(10)
    else:
        print(c)