# https://solved.ac/profile/playdev7

# 1157 - 단어 공부
# 문제
# 주어진 문자열에서 가장 많이 사용된 알파벳을 대문자로 출력한다.
# 대소문자 구분 없이 동일한 알파벳으로 간주한다.
# 가장 많이 사용된 알파벳이 동일할 경우 ? 을 출력한다.

st = input()
st = st.upper()
st = sorted(list(st))

st2 = set(st)

st_dict = dict()

for i in st2:
    st_dict[i] = st.count(i)

st_dict = sorted(st_dict.items(), key = lambda x : x[1], reverse=True)

try:
    print("?") if st_dict[0][1] == st_dict[1][1] else print(st_dict[0][0])
except:
    print(st_dict[0][0])