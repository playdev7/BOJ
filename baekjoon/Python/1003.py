# https://solved.ac/profile/playdev7
# 1003 - 피보차니 함수

# 문제
# 피보나치 함수에 특정 값을 넣었을 때 0이 출력되는 횟수와 1이 출력되는 횟수를 구하여라

# 풀이
# 0 = 1, 0 으로 시작해서
# 1 = 0, 1 / 2 = 1, 1 / 3 = 1, 2 / 4 = 2, 3 이 되는 특성이 있다.
# 즉 0, 0 부터 b, a+1 이 반복된다.

zero, one = 0, 0
fibonacci_list = [[1, 0], [0, 1], [1, 1]]

def dp_fibonacci(num):
    for i in range(3, num+1):
        a, b = fibonacci_list[-1]
        fibonacci_list.append([b, a+b])        
    print(f"{fibonacci_list[num][0]} {fibonacci_list[num][1]}")
    
testcase = int(input())

for test in range(testcase):
    test = int(input())
    dp_fibonacci(test)