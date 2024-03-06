# 31497 / 생일 축하합니다~
# 인터랙션 애드훅
# 애드훅? 특정 문제에 국한되어 해결되게 만든 국소적 PS 프로그램

# 이름의 개수 n이 주어짐
# n개의 이름이 주어짐
# 이후 아래 규칙으로 인터랙션
    # `? x` 꼴로 질문
    # 생일이면 1, 아니면 0 출력
    # 최대 1000번까지 질문 가능

# 입출력 규칙
# sys로 입력받아야 함
# 출력 후 플러시로 비워줘야 함

import sys
n = int(sys.stdin.readline())
names = [sys.stdin.readline() for i in range(n)]

for i in range(333):
    i = i % len(names)
    cnt = 0
    for j in range(3):
        print("? " + names[i], flush = True)
        a = int(sys.stdin.readline())
        if a == 1:
            cnt += 1
        if cnt == 2:
            print("! "+names[i], flush=True)
            exit()