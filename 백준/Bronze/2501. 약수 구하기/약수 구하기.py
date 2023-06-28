N, K = map(int, input().split())
measures = list()
for i in range(1, N+1):
    if N % i == 0:
        measures.append(i)
else:
    try:
        print(measures[K-1])
    except:
        print(0)