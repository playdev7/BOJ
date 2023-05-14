# https://solved.ac/profile/playdev7
# 13241 - 최소공배수

# 문제 - 공백을 기준으로 두 정수가 입력되면 최소공배수를 출력하는 프로그램 작성.
# 입력 - 한 수는 1000보다 작고 한 수는 1000보다 크고 10**8 보다 작다.

# 최소공배수는 두 수의 곱 / 최대공약수로 구할 수 있다.
# 왜냐하면, 최소공배수 * 최대공배수는 두 수의 곱과 같다.
# 궁금하면 화이트보드에 그려보면 된다.

# 최대공약수는 유클리드 호제법을 통해서 쉽고 빠르게 구하자.
# 유클리드 호제법 - p와 q 중에서 큰 수가 p, 작은 수가 q 가 된다.
# 이후 p에는 q를 대입하며 q에는 p%q를 대입한다.
# q가 0이 되는 순간에 나오는 p가 최대공약수이다.

def GCD(p, q):
    while q > 0 :
        p, q = q, p % q
        GCD(p, q)
    
    return p

def main():
    a, b = map(int, input().split())
    if a < b:
        print(int(a * b / GCD(b, a)))
    else:
        print(int(a * b / GCD(a, b)))

if __name__ == "__main__":
    main()