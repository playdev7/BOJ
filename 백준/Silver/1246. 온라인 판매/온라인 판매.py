# https://solved.ac/profile/playdev7
# 1246 - 온라인 판매
# 문제
# n개의 계란이 있고 m명의 고객이 있을 때 최대수익과 최저가의 달걀 가격
# m명의 고객은 각자 자기가 구매 가능한 상한가가 있음

n, m = map(int, input().split())
prices = [int(input()) for _ in range(m)]
prices.sort(reverse=True)

max_revenue = -1
price = 99999999999

for i in range(len(prices)):
    j = i
    if j > n-1:
        j = n-1
    if max_revenue < prices[i] * (j+1):
        max_revenue = prices[i] * (j+1)
        price = prices[i]
    if max_revenue == prices[i] * (j+1):
        if price > prices[i]:
            price = prices[i]
else:
    print(price, max_revenue)