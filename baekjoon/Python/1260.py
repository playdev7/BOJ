# https://solved.ac/profile/playdev7
# 1260 / DFS와 BFS

# 문제
# 정점과 간선, 시작정점이 주어지면 각각 DFS와 BFS를 진행한 결과를 출력하는 프로그램
# 동일 레벨일 경우 정점번호가 작은 것을 먼저 방문한다.

# 입력 - 정점의 개수 N, 간선수 M, 시작정점 R 이 주어진다
    # 이후 M개의 줄동안 u v 를 잇는 간선의 정보가 주어진다.
# 출력 - 첫 줄에 DFS 결과를, 둘째줄에 BFS 결과를 출력한다.
    # 시작정점부터 방문한 정점을 차례대로 출력하면 된다.

# sys.stdin.readline() 위한 sys 모듈 삽입
import sys
# M의 입력은 10**4 => 기본 재귀 한도가 10**3(1000)으로 제한되어 있으므로 10**8 로 상향.
sys.setrecursionlimit(10**8)

# deque 객체 삽입
from collections import deque

# BFS - 큐에서 시작 정점 꺼내고 해당 정점의 인접 노드 방문하여 큐에 넣고
# 위 작업을 큐가 완전히 사라질 때 까지 반복하도록.
def BFS(n, graph, start):
    
    visited = [False] * (n + 1)
    visited[start] = True
    path = list()
    
    queue = deque()
    queue.append(start)
    path.append(start)

    try:
        while queue:
            q = queue.popleft()
            for v in graph[q]:
                if visited[v] == False:
                    visited[v] = True
                    queue.append(v)
                    path.append(v)
    except:
        pass

    return path

# DFS - 계속 재귀하며 시작 정점과 연결된 노드들을 재귀하며 탐색.
def DFS(visited, graph, start):
    visited[start] = True
    global dfs_path
    dfs_path.append(start)

    try:
        for i in graph[start]:
            if visited[i] == False:
                DFS(visited, graph, i)
    except:
        pass

    return dfs_path

def main():
    n, m, r = map(int, sys.stdin.readline().strip().split())
    graph = dict()

    for i in range(m):
        u, v = map(int, sys.stdin.readline().strip().split())
        if u in graph:
            graph[u].append(v)
        else:
            graph[u] = [v]
        if v in graph:
            graph[v].append(u)
        else:
            graph[v] = [u]

    for i in graph:
        graph[i].sort()

    # DFS 는 재귀를 하므로 방문리스트와 경로를 외부에 선언해주어야 함.
    global dfs_path
    dfs_path = list()
    global dfs_visited
    dfs_visited = [False] * (n+1)


    ans1 = DFS(dfs_visited, graph, r)
    ans2 = BFS(n, graph, r)

    print(*ans1)
    print(*ans2)

    return 0

if __name__ == "__main__":
    main()