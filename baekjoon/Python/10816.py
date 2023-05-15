# https://sovled.ac/profile/playdev7
# 숫자 카드 2 - 10816

# 문제 - 번호가 부여되어있는 카드가 있다.
# 상근이는 n 개의 카드를 가지고 있다. 카드의 번호는 중복될 수 있다. 
# 이후 m 개의 카드 번호 가 주어졌을때, 상근이가 m1, ... 번째에 몇 개의 카드를 가지고 있는지 순차적으로 출력하는 프로그램.

# 입력
# 1행 - 상근이가 가진 카드의 수
# 2행 - 상근이가 가진 카드의 번호 목록 0 -10^6 ~ 10^6
# 3행 - 개수를 찾고 싶은 카드의 수
# 4행 - 개수를 찾고 싶은 카드의 번호 목록 -10^6 ~ 10^6

# 출력
# 공백을 기준으로 구분하여 m개의 정수를 출력한다.
# 풀이 시작

# 풀이 핵심 - 최선의 알고리즘 만큼 시간을 최대한 줄이는 출력방향성을 잡아야한다.
def main():
    # n 입력 받음
    n = int(input())

    # 값이 중복될 수 있으므로 리스트로 입력받는다.
    # 이후 빠른 탐색을 위해 딕셔너리도 생성한다.
    n_list = list(map(int, input().split()))
    n_dict = dict()

    # n_list 를 대입하며 n을 n_dict의 키로 부여한다.
    # n이 키로 존재하지 않으면 해당 value로 1을 부여한다.
    # n이 키로 존재하면 해당 value 를 1 증가시킨다.
    for n in n_list:
        if n in n_dict:
            n_dict[n] += 1
        else:
            n_dict[n] = 1

    # 이후 m과 m_list에 대한 입력을 받는다.
    m = int(input())
    m_list = list(map(int, input().split()))

    # m_list 를 대입하며 n_dict에 m이 키로 존재하는지 확인한다.
    # 존재한다면 해당 value를 정답으로 출력한다.
    # 존재하지 않는다면 0을 정답으로 출력한다.
    for m in m_list:
        if m in n_dict:
            print(n_dict[m], end = " ")
        else:
            print(0, end = " ")

if __name__ == "__main__":
    main()