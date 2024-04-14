# 스트링 편집거리 문제
# 삽입: A의 한 위치에 문자 하나를 삽입한다.
# 삭제: A의 문자 하나를 삭제한다.
# 교체: A의 문자 하나를 다른 문자로 교체한다.

# 입력은
    # 문자열 X
    # 문자열 Y
    
# 출력
    # 최소횟수
    
x = input()
y = input()

def string_edit_distance(str1, str2):
    # len(str1)*len(str2) 의 Matrix
    dp = [[0] * (len(str2)+1) for _ in range(len(str1) + 1)]
    # 각 행의 첫 원소는 행번호 = range(1, len(x)+1)
    for i in range(1, len(str1)+1):
        dp[i][0] = i
    # 첫행의 원소는 열번호 range(1, len(y)+1)
    for j in range(1, len(str2)+1):
        dp[0][j] = j

    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            # 한 쪽이 0이면
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            
            # 이외에는 점화식(최적성의 원리)
            else:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

    return dp[-1][-1]

print(string_edit_distance(x, y))