# https://solved.ac/profile/playdev7
# 24444 / 알고리즘 수업 - 너비 우선 탐색 1

# 문제
# N개의 정점과 M개의 간선으로 구성된 무방향 그래프가 주어진다.
# BFS 하여 노드의 방문 순서를 출력한다.

# 입력
# 첫 줄에 공백을 기준으로 N M R이 주어진다. - 정점 수, 간선 수, 시작정점
# 다음 M개의 줄에 간선 정보 u v 가 주어진다. - 가중치가 1인 양방향 간선이다.

# 출력
# N개의 줄 동안 i번 노드가 몇 번째로 방문했는지 1번부터 차례대로 출력한다.

# sys 모듈 탑재. sys.stdin.readline() 사용을 위해서.
import sys 
# collections 라이브러리의 deque 사용.
from collections import deque


# 정답 딕셔너리 및 정답 카운터 생성
global answer
answer = dict()
global cnt 
cnt = 1

# BFS 함수
def BFS(adj, start):
    # 탐색용 deque 선언 - exp
    exp = deque()

    # 시작 정점 먼저 담고 방문표시.
    exp.append(start)
    visited[start] = True

    # answer에 경로 추가.
    # 현재정점 [Key] 이 : n회차다 value
    global answer
    global cnt
    answer[start] = cnt
    
    # deque가 소진될 때 까지.
    # 현재 큐에 먼저 들어온 요소를 뺸다.
    # 해당 노드에 접근하여 인접리스트를 확인한다.
    # 방문처리 되지 않았다면 해당 요소를 방문처리한다.
    # 그리고 큐에 넣는다.
    while exp:
        q = exp.popleft()
        for i in adj[q]:
            if visited[i] == False:
                visited[i] = True
                exp.append(i)
                cnt += 1
                answer[i] = cnt
                
    return 0

def main():
    N, M, R = map(int, sys.stdin.readline().strip().split())
    
    # 인접 딕셔너리 생성.  
    adj_list = [[] for _ in range(N+1)]

    for i in range(M):
        u, v = map(int, sys.stdin.readline().strip().split())
        adj_list[u].append(v)
        adj_list[v].append(u)

    # 동일 레벨에 대한 오름차순 정렬.
    for i in range(1, len(adj_list)):
        adj_list[i].sort()

    # 방문 리스트 생성 - 1부터 N+1 까지 사용할 것이다.
    global visited
    visited = [False] * (N+1)
    visited[0] = True

    # BFS 실행
    BFS(adj_list, R)
    
    # 정답 딕셔너리에 대한 출력
    # 해당 노드가 없으면 0을 출력.
    for i in range(1, N+1):
        if i in answer:
            print(answer[i])
        else:
            print(0)

if __name__ == "__main__":
    main()