# https://solved.ac/profile/playdev7
# 10716 - 딸기당근수박참외메론게임 / 네블컵

# 문제
# n개의 단어를 b번의 리듬에 맞춰 게임을 진행한다.
# 1부터 b까지 늘어나며 단어를 말하고, 다시 2까지 줄어들며 말하는 패턴을 반복한다.
# 특정단어가 x번째 말할 때 이 게임은 몇회차인가?

import sys

n, b = map(int, input().split())
word, x = input().split()
x = int(x)
words = sys.stdin.readline().strip().split()

games = 0

while len(words) < b:
    for i in words:
        if len(words) == b:
            break
        words.append(i)

cnt = 0

while cnt < x:
    for i in range(b):
        if cnt > x:
            break
        if word in words[:i+1]:
            cnt += words[:i+1].count(word)
        games += 1

    else:
        for i in range(b-1, 1, -1):
            if cnt > x:
                break
            if words[:i]:
                cnt += words[:1].count(word)
            games += 1

print(words, games)