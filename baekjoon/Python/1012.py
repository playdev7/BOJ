# https://solved.ac/profile/playdev7
# 1012 / 유기농 배추

# 문제
# 상하좌우로 인접한 배추집합이 몇 개나 되는지 출력하는 프로그램

# 입력
# 테스트 케이스의 개수 T가 주어진다.
# 이후 T가 시작되는 지점에서 M N K(배추가 심긴 개수) 가 주어진다.
# 이후 K 줄 동안 x y 가 주어진다.
# M이 열, N이 행이 된다..

# 출력
# T줄에 거쳐 각 테스트 케이스에 대한 배추집합의 개수를 출력한다.

# 풀이 - 배추를 찾으면 1을 누산하고, 인접한 배추집합을 0으로 만들어버린다.
    # 어떻게? DFS로 재귀해서 상하좌우 싹 다 0 으로.

# 재귀 범위 제한 1000 -> 10**8
import sys
sys.setrecursionlimit(10**8)

# 배추가 있는 좌표와 농장을 받아서 재귀하는 DFS 함수
def explorer(x, y):
    # 상하좌우 - dynamic x, dynamic y
    dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]

    # farm 전역 변수 활용함을 선언
    global farm

    # 보이는 그대로 배추를 찾은 지점을 상하좌우로 돌면서 싹 다 0으로 만든다.
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if -1 < nx < len(farm[0]) and -1 < ny < len(farm):
            if farm[ny][nx] == 1:
                farm[ny][nx] = 0
                explorer(nx, ny)
    
    return 0

def main():
    # 테스트 케이스 T를 입력받는다.
    T = int(input())

    # 정답은 테스트 케이스 개수만큼 출력하므로 리스트로 선언한다.
    answer = list()

    # T만큼 반복하며 아래와 같이 작동한다.
    for T in range(T):
        # 농장의 사이즈와 배추의 개수를 입력받는다.
        M, N, K = map(int, sys.stdin.readline().strip().split())
        
        # N*M 사이즈의 농장을 지어준다. 나는 M*N 행렬이 좋은데 자꾸 N*M 이라고 해서 헷갈린다.
        # 글로벌 변수로 선언한다.
        global farm
        farm = [[0] * M for _ in range(N)]

        # 이번 케이스에서 배추집합의 갯수 세어줄 cnt를 선언한다.
        cnt = 0

        # x, y 좌표를 sys.stdin.readline 으로 빠르게 입력받는다.
        # strip은 양쪽 다 개행문자나 공백을 제거해주는 메소드이다. 자매품으로 lstrip과 rstrip이 있다.
        # farm은 n*m 행렬이므로 [y][x]로 인덱싱하여 배추를 1로 심어준다.
        for i in range(K):
            x, y = map(int, sys.stdin.readline().strip().split())
            farm[y][x] = 1

        # 탐색은 인덱스 번호만 맞으면 되므로 x, y 순으로 탐색한다.
        # 1이 발견되면 cnt를 1 올리고 explorer를 실행한다.
        # explorer 는 앞서 기재한 바와 같이 인접한 모든 배추를 싹 다 0으로 만드는 재귀 함수이다.
        for x in range(M):
            for y in range(N):
                if farm[y][x] == 1:
                    explorer(x, y)
                    cnt += 1

        answer.append(cnt)

    print(*answer, sep = "\n")

if __name__ == "__main__":
    main()