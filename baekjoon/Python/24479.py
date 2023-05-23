# https://solved.ac/profile/playdev7
# 24479 / 알고리즘 수업 - 깊이 우선 탐색 1

# 문제
# n개의 정점과 m 개의 간선으로 구성된 무방향 그래프가 주어진다.
# 정점번호는 1부터 N까지이다. 모든 간선의 가중치는 1이다.
# 정점 R부터 DFS로 모든 노드를 방문한다.
# 중요 - 같은 레벨일 경우 오름차순으로 방문한다.

# 입력 - 첫 줄에 정점 수 N, 간선 수 M, 시작정점 R 이 공백을 기준으로 주어진다.
    # 이후 M개의 줄 동안 공백을 기준으로 u v 를 잇는 간선 정보가 주어진다.
# 출력 - 각 정점의 줄마다 개행하며 아래와 같이 출력한다.
    # i번째 줄에 i번 정점이 방문한 정점 출력.

# 풀이
# 문제 핵심 - 이미 인접리스트가 주어진다. 그리고 재귀하면 된다는 것을 알려준다.

# sys 라이브러리 import
import sys

# 재귀 깊이 부여
sys.setrecursionlimit(10**9)


# DFS 부분 - (VErtex(정점), Edge(간선), R(시작점))
def DFS(V, E, R):  
    visited[R] = True

    global cnt
    path[R] = cnt
    cnt += 1

    for x in E[R]:
        if visited[x] == False:
            DFS(V, E, x)

    return 0


def main():
    # Node, M(간선), R(시작점) 및 인접리스트 받기
    N, M, R= map(int, sys.stdin.readline().strip().split())
    
    # 리스트 형태의 그래프 선언.
    # 원활한 연산을 위해 1부터 N까지 사용할 수 있도록 N+1의 길이 지정
    graph = [[] for _ in range(N+1)]

    # 실제 인접리스트 만들기.
    # 빠른 입력 받기 위해 stdin.readline 통한 입력.
    # 양방향 그래프 이므로 아래와 같이 코딩.
        # u 정점에는 v가, v정점에는 u가 서로가 서로에게 대입되도록 코딩.
    for i in range(M):
        u, v = map(int, sys.stdin.readline().strip().split())
        graph[u].append(v)
        graph[v].append(u)

    # 동일 레벨에서는 숫자가 작은쪽으로 간다고 하였으므로 오름차순 정렬.
    for i in range(1, len(graph)):
        graph[i].sort()

    # 방문리스트 전역변수로 선언
    global visited
    visited = [False] * (N + 1)

    # 경로 딕셔너리 선언 및 번호 부여 위한 cnt 변수 선언
    global path
    path = dict()
    global cnt
    cnt = 1

    # DFS 실행.    
    DFS(N, graph, R)


    for i in range(1, N+1):
        if i not in path:
            print(0)
        else:
            print(path[i])

    return 0

if __name__ == "__main__":
    main()