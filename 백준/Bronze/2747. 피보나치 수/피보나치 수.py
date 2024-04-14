# n이 주어졌을 때 n번째 피보나치 수를 구하는 프로그램 작성
# 점화식
    # 0=0
    # 1=1
    # 2~ => Fn = F(n-1) + F(n-2)

# DP의 핵심 => 연산 과정마다 최적해를 테이블에 담아버린다.
dp_table = [0, 1] # 1번째 연산, 2번째 연산은 0=0, 1=1 이므로 preset

def pivonachi(n):
    return dp_table[n-1] + dp_table[n-2]

n = int(input())

for i in range(2, n+1):
    dp_table.append(pivonachi(i))
    
print(dp_table[-1])