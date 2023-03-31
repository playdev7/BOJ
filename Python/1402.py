# 시간 초과 - 반복문 좀 더 줄여보자...

# 리스트 전역 변수로
prime_numbers = []

# A를 소인수 분해 할 함수 만들기
def factorization(num):
    i, j = 2, 0
    while num > 1:
        if num % (i+j) == 0:
            prime_numbers.append(i+j)
            num = num / (i+j)
        else:
            j += 1
    return prime_numbers

# 모든 소수 덧셈하는 함수 만들기
def total_prime_number(nums):
    total = 0
    for i in prime_numbers:
        total += i
    return total

def main():
    test = int(input())
    for i in range(test):
        a, b = input().split()
        a = int(a)
        b = int(b)
        a = factorization(a)
        if b == total_prime_number(a):
            print("yes")
        else:
            print("no")

if __name__ == "__main__":
    main()