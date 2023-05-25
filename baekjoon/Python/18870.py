# https://solved.ac/profile/playdev7
# 18870 / 좌표 압축

# 문제
# 수직선 상의 좌표가 주어지면 가장 작은수를 0, 다음수를 1씩 증가시키며 좌표를 압축시키는 문제.

# 입력
# 첫 줄에 대상 수의 개수가 주어진다.
# 이후 공백을 기준으로 N개의 수가 주어진다.

# 출력
# 한 줄에 공백을 기준으로 입력된 각 수의 좌표압축 결과를 출력한다.

import sys

n = int(input())
x_list = list(map(int, sys.stdin.readline().strip().split()))
sort_x = sorted(x_list)

x_dict = dict()

cnt = 0

for i in sort_x:
    if i in x_dict:
        cnt -= 1
    x_dict[i] = cnt
    cnt += 1
    
    
for i in x_list:
    print(x_dict[i], end = " ")