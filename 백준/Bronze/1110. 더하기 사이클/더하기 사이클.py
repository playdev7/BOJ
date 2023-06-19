# https://solved.ac/profile/playdev7
# 1110 - 더하기 사이클

# 문제
# 한자리라면 뒤에 0을 붙인 두자리 수 N에 대해 각 자리의 수를 더한다.
# 한자리가 되면 직전 일의자리 수를 붙인다.
# 원래의 수가 되는 회차 출력

N = input()

if len(N) == 1:
    N += "0"

N2 = N

N2 = N2[-1] + str(int(N2[0]) + int(N2[1]))[-1]

cnt = 1

while N2 != N:
    N2 = N2[1] + str(int(N2[0]) + int(N2[1]))[-1]
    cnt += 1

else:
    print(cnt)