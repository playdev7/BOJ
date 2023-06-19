# https://solved.ac/profile/playdev7
# 1259 - 팰린드롬수

# 문제
# 주어지는 숫자가 팰린드롬이면 "yes", 아니면 "no"를 출력하는 프로그램
# "0" 이 입력되면 종료한다.

test = str()

while test != "0":
    test = input()
    result = test[::-1]

    if test == "0":
        break
    elif test == result:
        print("yes")
    else:
        print("no")