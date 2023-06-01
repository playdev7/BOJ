# https://solved.ac/profile/playdev7
# 2577 - 숫자의 개수

# 문제
# A B C가 주어지면 A * B * C 의 값에서 0-9 가 각각 몇개인지 출력

# 입력
# A B C가 세 줄에 거쳐 입력된다.

# 출력
# 0부터 9까지 10줄에 거쳐 해당 수가 몇 개 포함되는지 출력한다.

A = int(input())
B = int(input())
C = int(input())

print(list(str(A * B * C)).count('0'))
print(list(str(A * B * C)).count('1'))
print(list(str(A * B * C)).count('2'))
print(list(str(A * B * C)).count('3'))
print(list(str(A * B * C)).count('4'))
print(list(str(A * B * C)).count('5'))
print(list(str(A * B * C)).count('6'))
print(list(str(A * B * C)).count('7'))
print(list(str(A * B * C)).count('8'))
print(list(str(A * B * C)).count('9'))