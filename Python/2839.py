# https://solved.ac/profile/playdev7
# 2839 - 설탕 배달

# 3kg 봉투와 5kg 봉투가 있다.
# 설탕을 정확히 N 킬로그램 배달해야 할 때, 봉지를 몇 개 가져가야 하는지 출력하라.
# 정확히 배달 할 수 없다면, -1 을 출력한다.
# np-완전문제인 듯 아닌 배낭문제

kg = int(input())

big = 5
small = 3
cnt = 0

while kg > 0:
    if kg % big == 0:
        kg -= big
        cnt += 1
    else:
        kg -= small
        cnt += 1

if kg < 0:
    print(-1)
else:
    print(cnt)