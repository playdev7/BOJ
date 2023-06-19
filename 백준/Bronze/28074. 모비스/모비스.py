# https://solved.ac/profile/playdev7
# 2023 인하대학교 프로그래밍 경진대회(IUPC) Open Contest
# A번 - 모비스

# 주어진 문자열로 "MOBIS" 를 만들 수 있는지 확인하는 프로그램

string = set(input())

if "M" in string and "O" in string and "B" in string and "I" in string and "S" in string:
    print("YES")
else:
    print("NO")