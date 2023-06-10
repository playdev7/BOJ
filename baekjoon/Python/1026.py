# https://solved.ac/profile/playdev7
# 1026 - 보물

# 문제
# N개의 정수를 가진 리스트가 있다.
# A집합에 N개의 수가 주어진다.
# B집합에 N개의 수가 주어진다.
# B집합의 위치는 변경할 수 없다.
# A집합의 위치를 재배열하여 아래 공식의 최소값을 만들어라.
# A[0]*B[0] + A[1]*B[1] + ... A[n] * B[n]

# 풀이
# 말장난일 뿐 결국 가장 작은수와 가장 큰 수로 정렬하고 합해주면 된다.
# 왜냐하면 어차피 A를 최적으로 재배치하면 끼워맞춰지기 때문이다.

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort(reverse=True)

result = 0

for i in range(N):
    result += A[i] * B[i]

print(result)