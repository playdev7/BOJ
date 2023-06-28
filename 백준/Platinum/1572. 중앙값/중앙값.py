import sys
input = sys.stdin.readline
import heapq

N, K = map(int,input().split())

maxHQ = list()
minHQ = list()
heapq.heappush(maxHQ, (10**9, 10**9))
heapq.heappush(minHQ, (10**9, 10**9))

middle = [0]*N
result = 0

for i in range(N):
  n = int(input())
  middle[i] = n
  if n > minHQ[0][0]:
    heapq.heappush(minHQ, (n,i))
  else:
    heapq.heappush(maxHQ, (-n,i))

  if i >= K:
    if maxHQ[0][1] == i-K:
      heapq.heappop(maxHQ)
    elif minHQ[0][1] == i-K:
      heapq.heappop(minHQ)
    else:
      if middle[i-K]>minHQ[0][0]:
        heapq.heappush(maxHQ, (10**9, 10**9))
      else:
        heapq.heappush(minHQ, (10**9, 10**9))
  
  while True:
    if maxHQ[0][1] <= i-K:
      heapq.heappop(maxHQ)
      heapq.heappush(maxHQ, (10**9, 10**9))
      continue
    if minHQ[0][1] <= i-K:
      heapq.heappop(minHQ)
      heapq.heappush(minHQ, (10**9, 10**9))
      continue
    if len(minHQ) > len(maxHQ):
      v,j = heapq.heappop(minHQ)
      heapq.heappush(maxHQ, (-v,j))
      continue
    if len(maxHQ) > len(minHQ)+1:
      v,j = heapq.heappop(maxHQ)
      heapq.heappush(minHQ, (-v,j))
      continue

    if i>=K-1:
      result -= maxHQ[0][0]
    
    break
  
print(result)