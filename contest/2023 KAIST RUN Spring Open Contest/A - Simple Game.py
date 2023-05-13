# https://solved.ac/profile/playdev7
# 2023 KAIST RUN Spring Open Contest
# A번 - Simple Game

# 문제 - 아래 등차수열이 성립하는지 증명하는 프로그램.
# 조건 - 첫째 항이 a이고, 공차가 b이다.
# 조건 - 원소는 n개이고, 각 원소는 서로소여야 한다.

# 입력 - n, a, b가 주어진다
# 출력 - 조건이 맞으면 Yes, 아니면 No 출력
# Yes 일 경우 등차수열의 원소를 n 줄에 거쳐서 출력하면 된다.
# 풀이 -> a 와 b 가 서로소이면 서로소인 등차수열이 성립한다..

# 유클리드 호제법 통한 GCD 찾기. - 1이면 "Yes", 1 초과하면 "No"
def GCD(a, b):
    while(b):
        a, b = b, a % b
    return a
                
def make_sequence(n, a, b):
    # 홀수에서 끊는다.
    for i in range(2*n):
        if i == 0:
            print(a, end=" ")
        elif i % 2 == 1:
            print(a + (b*i))
        else:
            print(a + (b*i), end=" ")  
    return 0

def main():
    n, a, b = map(int, input().split())
    result = GCD(a, b)
    
    if result > 1:
        print("No")
    else:
        print("Yes")
        make_sequence(n, a, b)
    

if __name__ == "__main__":
    main()