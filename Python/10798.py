# https://solved.ac/profile/playdev7
# 10798 - 세로 읽기
# 문제 해석 - 2차원 배열을 입력받아서 세로로 출력해라.

# 2차원 배열 string_map 생성
# 공백 없는 하나의 문자열이 5줄에 거쳐 입력된다.
string_map = [list(input()) for y in range(5)]

# string_map 의 하위 배열 중에서 가장 긴 배열을 구하여 width에 저장한다.
width = len(string_map[-1])

for i in string_map:
    if width < len(i):
        width = len(i)

# 이후 각 배열에 대해 0부터 width까지 인덱스를 우선으로 출력시킨다.
else:    
    for i in range(width):
        for j in string_map:
            try:
                # end 키워드를 활용하여 개행 없이 이어서 쭉 출력시킨다.
                print(j[i], end="")
            except IndexError:
                # 각 배열의 길이는 다르므로, IndexError가 발생한다. 예외처리로 pass 시킨다.
                pass