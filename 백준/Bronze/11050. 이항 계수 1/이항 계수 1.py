# 11050 이항계수 1
# N, K가 주어졌을때 이항계수 nCk를 구하는 프로그램을 작성하시오.
# nCk = n! / (k! * (n-k)!)

def factorial(n):
    val = 1
    for i in range(1, n+1):
        val *= i
    return val

n, k = map(int, input().split())
print(factorial(n) // (factorial(k) * factorial(n-k)))