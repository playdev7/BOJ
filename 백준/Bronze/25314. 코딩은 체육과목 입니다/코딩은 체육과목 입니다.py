# https://solved.ac/profile/playdev7
# 25314 - 코딩은 체육과목 입니다
# 문제
# 4바이트는 long int 이다.
# 4바이트마다 long 이 추가된다.
# 임의의 바이트 수가 주어졌을 때 얼마나 긴 자료형이 필요한지 출력한다.

result = ""
for _ in range(int(input()) // 4):
    result += "long "
    
print(result + "int")