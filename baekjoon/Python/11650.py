# https://solved.ac/profile/playdev7
# 11650 - 좌표 정렬하기

# N개의 점이 [x, y] 로 입력된다
# 1. x좌표가 증가하는 순으로 정렬한다.
# 2. 이후 X좌표가 같으면 y좌표가 증가하는 순으로 정렬한 다음 출력한다.

# 풀이 시작

n = int(input())

coords = [list(map(int, input().split())) for _ in range(n)]

# Python의 sort() 메소드는 각 배열의 첫 요소를 기준으로 오름차순 정렬함.
# 그리고 첫 요소가 같으면 자동으로 다음 요소를 기준으로 오름차순 정렬 함...
coords.sort()

for i in coords:
    print(i[0], i[1])