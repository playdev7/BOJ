# https://solved.ac/profile/playdev7

# 2609 - 최대공약수와 최소공배수

# 문제
# 공백을 기준으로 두 수가 주어진다.
# 첫 줄에 GCD, 다음줄에 LCM을 출력한다.

# 풀이
# GCD는 유클리드 호제법을 활용한다.
# GCD * LCM = 두 수의 합.

def GCD(p, q):
    if q == 0:
        return p
    else:
        return GCD(q, p % q)

A, B = map(int, input().split())
print(GCD(A, B))
print((A * B) // GCD(A, B))