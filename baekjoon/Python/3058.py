# https://solved.ac/profile/playdev7
# 3058 - 짝수를 찾아라

# 문제
# 7개의 자연수가 주어질 때 짝수의 합과 짝수 중 최솟값을 출력하는 프로그램

T = int(input())

for _ in range(T):
    nums = list(map(int, input().split()))
    evens = list()
    for num in nums:
        if num % 2 == 0:
            evens.append(num)
    print(f"{sum(evens)} {min(evens)}")