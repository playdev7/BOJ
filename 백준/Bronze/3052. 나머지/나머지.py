# https://solved.ac/profile/playdev7
# 3052 - 나머지
# 문제
# 주어진 10개의 수에 대해 42로 나눈 나머지의 개수를 출력한다.
# 풀이 - set 객체는 중복을 허용하지 않는다.
# set 객체에 담은 다음 크기를 출력한다.

result = set()
for i in range(10):
    result.add(int(input()) % 42)

print(len(result))