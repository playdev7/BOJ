# https://solved.ac/profile/playdev7
# 2023 SCON Open Contest
# C번 - 등차수열의 합

# 길이가 N인 수열에 대한 등차수열 A가 있다.
# 길이가 똑같은 등차수열인 B와 C로 쪼갤 수 있느냐.
# 등차수열이면 무조건 "YES", 아니면 "NO"

N = int(input())

A = list(map(int, input().split()))
B = [0] * N
C = [0] * N

if N == 1:
    print("YES")
    print(int((A[0]) * - 1))
    print(int((A[0]) * 2))

else:
    check = A[1] - A[0]

    for i in range(1, N):
        if A[i] - A[i-1] != check:
            print("NO")
            break
    else:
        print("YES")
        for i in range(N):
            B[i] = A[i] * 2

        for i in range(N):
            C[i] = A[i] * -1
        print(*B)
        print(*C)