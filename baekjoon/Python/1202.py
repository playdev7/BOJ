# https://solved.ac/profile/playdev7
# 1202 - 보석 도둑

# 배낭문제
# N개의 보석이 있고 무게 M과 가격 V가 주어진다.
# 가방 K개가 있고, 가방 하나에는 하나의 보석씩만 넣을 수 있다.
# 문제 핵심 - 가방 하나에는 하나의 보석씩만 넣을 수 있다.

# 입력
# 첫 줄에 N과 K가 주어진다.
# 이후 N줄동안 보석의 무게 M 과 가격 V 가 주어진다.
# 이후 K줄동안 적재가능 무게 C가 주어진다.

# 출력
# 훔친 보석 가격의 최대합을 출력한다.

# 풀이
# 힙 자료구조를 활용한 욕심쟁이 기법 적용.
# 중간 중간 주석으로 풀이과정 서술함.

import sys
input = sys.stdin.readline
import heapq

# 보석의 수 N 과 가방의 수 K
N, K = map(int, input().split())

# 훔친 결과
result = 0

# 보석 입력 받기 - 원소를 튜플로서 (무게, 가치) 가 되도록 만든다.
# 오름차순으로 정렬한다.
jewels = list()
for _ in range(N):
    m, v = map(int, input().strip().split())
    jewels.append((m, v))
jewels.sort()


# 가방 입력받기 - 비싼 보석이라고 무조건 무겁지는 않다.
# 따라서 가벼운 가방에서 가능한 비싼 보석을 뽑는 것이 좋다.
# 가방을 오름차순으로 정렬한다.
bags = list(int(input().strip()) for _ in range(K))
bags.sort()

# Priority Queue로서 최대힙을 만들어준다.
MaxHeap = list()
heapq.heapify(MaxHeap)

# 힙 자료구조
# 최대힙? 뭘 넣고 빼던 루트 노드가 항상 최대값인 자료구조.
# 최소힙? 뭘 넣고 빼던 루트 노드가 항상 최소값인 자료구조.
# Python heapq 라이브러리는 최소힙만 지원한다.
# 음수화 하여 삽입한다면? 가장 큰 값이 최소값이 된다.
# 즉, 음수화 하여 삽입하면 최대힙이 된다.

# 모든 가방을 하나씩 대입한다.
for bag in bags:
    
    # 현재 가방의 무게 이하인 보석을 모두 힙에 넣어준다.
    # 즉 내가 빼는 무게가 가방의 무게 이하일 때 까지만 반복한다.
    # 보석이 있어야만 훔칠 수 있으므로 지금 존재하는 보석의 개수까지만 반복한다.
    while len(jewels) > 0 and jewels[0][0] <= bag:
        
        # while문 조건 통과 - MaxHeap 에 jewels의 가격만 삽입한다.
        # heapq는 최소힙만 지원하므로 음수로 삽입하여 최대값을 최소값으로 인지하도록 속인다.
        heapq.heappush(MaxHeap, -jewels[0][1])
        
        # MaxHeap에 삽입이 되는 요소는 진입 시점에 "무게가 최솟값"을 가진 요소이다.
        # 즉 최소힙으로 나타내었을 경우 루트노드가 되었을 요소이다.
        # 보석은 하나만 훔칠 수 있으므로 반복문을 거쳐도 유일해야한다. 최소힙으로 만든 다음 루트노드를 빼어준다.
        heapq.heappop(jewels)
        
#### 이전에 삽입된 요소 또한 훔칠 대상이 되는 보석이다!!!!

    # 이후 MaxHeap의 최대값을 result에 누산한다.
    # 이전에 삽입된 요소 또한 훔칠 대상이 되는 보석이다. 따라서 바로 최대값을 구해주면 된다.
    # 최대힙의 최대값은 루트노드가 된다. 힙은 트리와 같은 자료구조로서 pop을 하면 루트노드가 빠진다.
    # 현재 힙의 값은 음수로 되어있으므로 result에 뺄셈을 진행한다. -1을 곱한 다음 더해주어도 무관하다.
    else:
        # 당연히 MaxHeap에 내용물이 들어있어야 꺼낼 수 있다.
        if len(MaxHeap) > 0:
            result -= heapq.heappop(MaxHeap)

print(result)