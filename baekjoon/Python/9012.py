# https://solved.ac/profile/playdev7

# 9012 - 괄호

# 문제
# "(" 와 ")" 로만 이루어진 문자열이 주어진다.
# 모든 괄호가 완전히 떨어지면 Yes, 아니면 No를 춞력한다.

N = int(input())
res = list()
for _ in range(N):
    queue = list(input())
    for _ in range(len(queue) // 2):
        try:
            for i in range(len(queue)):
                if queue[i] == "(" and queue[i+1] == ")":
                    queue.pop(i)
                    queue.pop(i)
        except:
            pass

    res.append(len(queue))
else:
    for r in res:
        print("YES") if r == 0 else print("NO")