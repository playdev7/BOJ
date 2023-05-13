# https://solved.ac/profile/playdev7
# 10951 - A+B - 4

# 문제 - 공백을 기준으로 입력되는 a, b 에 대해 A + B 를 출력하는 프로그램 제작
# 각 행이 테스트케이스가 되고, 테스트케이스 마다 A+B의 연산 결과를 출력하면 된다.
# 핵심 - 테스트 케이스의 개수가 명시되지 않음

# 풀이 시작

test_list = list()

# 무한 반복문에서 a, b가 입력되면 연산 결과를 바로 출력해준다.
# 런타임 에러가 발생할 경우 반복문을 즉시 종료하도록 한다.
while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except:
        break