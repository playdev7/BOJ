# https://solved.ac/profile/playdev7
# 2023 SCON Open Contest
# A번 - 정보섬의 대중교통

# n <= b 이므로 n은 고려하지 않음.

n, a, b = map(int, input().split())

if a > b:
    print("Subway")
    
elif a == b:
    print("Anything")
    
else:
    print("Bus")