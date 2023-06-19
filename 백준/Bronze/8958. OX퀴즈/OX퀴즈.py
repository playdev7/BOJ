# https://solved.ac/profile/playdev7
# 8958 - OX 퀴즈

# 문제 - O와X로만 이루어진 문자열이 입력되었을 때, O에 대한 연산 결과를 출력하는 프로그램 작성.
# 기본적으로 O가 있다면 1을 증가시킨다.
# 만약 O가 이전부터 누적되었다면, 누적된 숫자만큼 증가시킨다.

# 입력 - 첫 줄에 테스트 케이스의 개수 n, 다음 n개의 줄 만큼 "O","X" 가 담긴 공백없는 문자열이 입력된다.
# 출력 - n개의 행에 거쳐서 각 케이스에 대한 O의 개수를 출력시킨다.

# 풀이시작

n = int(input())
case = list(input() for _ in range(n))
result = list()

# 1. case를 대입한다.
for i in case:
    # 내부에 개수와 관련된 변수를 추가시킨다.
    # 이번 케이스의 최종 결과를 담을 res 변수.
    # 현재 O의 개수를 누적시키는 cnt 변수
    res = 0
    cnt = 0

    # 2. case에 담긴 문자열의 각 문자를 대입한다.
    # 2-1. 대입된 문자가 "O" 일 경우 cnt를 1 증가시킨다.
    # 2-2. 다음으로 res에 cnt를 추가시킨다.
    # 추가조건 - x가 발견될 경우 cnt를 0으로 초기화한다.
    for j in i:
        if j == "O":
            cnt += 1
            res += cnt
        else:
            cnt = 0

    # 3. 이후 result에 res를 원소로서 추가시킨다.
    result.append(res)

# 마지막으로 result를 순차적으로 대입하며 출력시킨다.
for r in result:
    print(r)