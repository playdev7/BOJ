# https://solved.ac/profile/playdev7
# 2023 서강대학교 청정수컵 Open Contest
# A번 - 레몬 따기

# 0에서 N까지 1씩 이동하며 최선의 선택에 대한 정답을 출력.
# 1. 이번 지점에서 모든 레몬을 딴다.
# 2. 다음 지점으로 이동한다.
# 추가조건 - 다음 지점으로 이동할 때 마다 레몬은 1씩 줄어든다.
# 마지막 인덱스에서도 집까지 1 이동해야 하므로 1이 줄어든다.

N = int(input())
lemons = list(map(int, input().split()))

lemon = 0

for i in range(N+1):
    lemon -= 1
    try:
        if lemons[i] > lemon:
            lemon = lemons[i]
    except:
        pass

print(lemon)