# https://solved.ac/profile/playdev7
# 2023 SCON Open Contest
# B번 - 팀명 정하기

# 1. 입학 연도를 오름차순으로 정렬해서 이어붙인 문자열
# 2. 성씨를 이니셜을 백준 랭킹이 높은 순으로 내림차순 나열한 문자열
# P Y S 순으로 해결한 문제수, 입학연도, 성씨가 주어진다.
# 총 3행인 배열이 온다.

team_list = list(input() for _ in range(3))

adm_list = list()

p_list = list()
p_dict = dict()

for i in team_list:
    p, y, s = i.split()
    adm_list.append(y[2:])
    p_list.append(int(p))
    p_dict[int(p)] = s[:1]
    
adm_list.sort()
print(adm_list[0]+adm_list[1]+adm_list[2])

p_list.sort(reverse = True)

for i in p_list:
    print(p_dict[i], end="")