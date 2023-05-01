# 입력된 숫자 중 최댓값과 최댓값의 행번호와 열번호 출력하기.
# 공백을 기준으로 9개의 수가 9라인 입력 되면 9 x 9 형태의 행렬로 만들어준다.
# 이후 원소 중 최댓값을 구하고, 해당 원소의 i,j 를 출력시키면 된다.

# 9 x 9 형태의 matrix 입력받기
matrix = [[int(x) for x in input().split()] for y in range(9)]

# matrix_max 변수 선언
matrix_max = max(matrix[0])

# max_i와 max_j 변수 선언
max_i, max_j = 0, 0

# 이후 matrix 의 최댓값 구하기
for i in range(1, len(matrix)):
    if max(matrix[i]) > matrix_max:
        matrix_max = max(matrix[i])
    else:
        pass        
else:
    for i in range(len(matrix)):
        if matrix_max in matrix[i]:
            max_i = i
            max_j = matrix[i].index(matrix_max)

print(matrix_max)
# 인덱스가 아닌 1부터 시작하는 자연수로 출력.
print(max_i+1, max_j+1)