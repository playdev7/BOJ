# https://solved.ac/profile/playdev7
# 2023-04-14 시간초과

# 입력받은 수를 인수분해 및 덧셈하는 함수 선언
def factorization(num):
    factors = []
    sum_factors = 0

    for i in range(1, num+1):
        # num의 약수면 약수 리스트에 추가
        if num % i == 0:
            factors.append(i)
            # num을 약수로 나눔
            num = num / i
    
    # 인수들에 대해 덧셈 진행.
    for i in factors:
        sum_factors += i
    
    # 인수들을 덧셈한 값을 반환
    return sum_factors


def main():
    test_case = int(input())
    for i in range(test_case):
        a, b = map(int, input().split())
        
        # 인수들을 덧셈한 값이 B와 일치하면 "yes" 출력
        if factorization(a) == b:
            print("yes")
        else:
            print("no")

if __name__ == "__main__":
    main()