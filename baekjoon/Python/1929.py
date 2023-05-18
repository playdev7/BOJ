# https://solved.ac/profile/playdev7
# 1929 - 소수 구하기

# 문제 - M 이상 N 이하의 모든 소수를 출력하는 프로그램
# TMI - 수열에서 2의 배수부터 모든 배수를 순차적으로 소거하는 기법을 에라토스테네스의 체 라고 한다.

# 입력 - 공백을 기준으로 M과 N이 주어진다.
# 출력 - 소수를 오름차순으로 개행하며 출력시킨다.

# 풀이 - 방문리스트처럼 접근하며 에라토스테네스의 체를 이용한다.
# n 까지 True인 리스트를 만든다.
    # 2의 배수부터 접근하며 인덱스의 값을 False로 만든다.

# 풀이 시작
def main():
    m, n = map(int, input().split())
    
    primes = [True] * (n + 1)
    primes[0] = False
    primes[1] = False

    for i in range(2, n+1):
        if primes[i] == True:
            for mix in range(i*2, n+1, i):
                primes[mix] = False
        if primes[i] == True:
            if i >= m:
                print(i)

if __name__ == "__main__":
    main()