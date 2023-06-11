# https://solved.ac/profile/playdev7
# 15596 - 정수 N개의 합

# 문제
# 정수 N개가 들어있는 리스트 a가 주어졌을 때 a의 모든 합을 반환하는 solve 함수 작성

# 언어제한
# Python 2, Python 3, PyPy, PyPy3: def solve(a: list) -> int
# a: 합을 구해야 하는 정수 n개가 저장되어 있는 리스트 (0 ≤ a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000)
# 리턴값: a에 포함되어 있는 정수 n개의 합 (정수)

def solve(a):
    ans = 0
    for i in a:
        ans += i
    return ans