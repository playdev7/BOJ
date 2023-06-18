# https://solved.ac/profile/playdev7

# 27959 - 초코바
# 문제
# 100원을 N개 갖고 있을 때 M원인 초코바를 먹을 수 있는가?
    # Yes or No 로 출력.

# 입력
# N과 M이 공백을 두고 주어진다.

# 출력
# Yes or No 로 출력한다.

N, M = map(int, input().split())
print("Yes") if N * 100 >= M else print("No")