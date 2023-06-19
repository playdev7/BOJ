n = int(input())
score = input()
scores = score.split()

# 자료형 하나가 큰 차이를 만듭니다..
scores = list(map(int, scores))
m = max(scores)

total = 0

for i in scores:
    total = total + i / m * 100

print((total / n))