# https://solved.ac/profile/playdev7
# 1620 - 나는야 포켓몬 마스터 이다솜

# 문제 - PK몬의 이름과 도감번호를 학습한 이후 퀴즈가 주어지면 정답을 출력하는 인공지능? 제작
# PK몬 이름은 대소문자를 구분하여 학습.
# 퀴즈 - PK몬 이름이 주어지면 도감번호를 답하고, 도감번호가 주어지면 PK몬 이름을 답해야 함.

# 입력 - 한 번에 아래의 내용이 순차적으로 들어옴.
# 첫 줄에 도감에 수록된 PK몬의 개수 N과 맞춰야 하는 문제수 M이 공백을 기준으로 주어짐.
# 이후 N개의 줄 만큼 PK몬의 이름이 주어짐
# 이후 M개의 줄 만큼 맞춰야 하는 퀴즈가 주어짐.

# 출력 - 입력된 M개의 줄 만큼 도감번호 or PK몬 이름을 순차적으로 출력

# 풀이 시작

# Python 알고리즘 핵심
# 리스트 자료형은 2번 인덱스를 지목해도 0, 1, 2 까지 접근을 하므로 시간복잡도가 O(n)이 된다.
# 딕셔너리는 키를 참고하면 바로 value를 출력하므로 시간복잡도가 O(1). 상수시간이다.


n, m = map(int, input().split())

# 도감번호와 PK몬 이름을 1부터 순차적으로 담는 딕셔너리 생성.
# PK몬 이름을 키로 하고, 도감번호를 값으로 하는 요소도 같이 담음.
poke_book = dict()
for i in range(1, n+1):
    poke_name = input()
    poke_book[str(i)] = poke_name
    if poke_name in poke_book:
        pass
    poke_book[poke_name] = str(i)

quiz = list()
for i in range(m):
    quiz.append(input())

for q in quiz:
    print(poke_book[q])