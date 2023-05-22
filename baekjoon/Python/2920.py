# https://solved.ac/profile/playdev7
# 2920 / 음계

# 1부터 8까지 차례대로 나오면 "ascending" 출력
# 8부터 1까지 차례대로 입력되면 "descending" 출력
# 그게 아니라면 "mixed" 출력

music = list(map(int, input().split()))

asc = 1
desc = 1
mix = 1

for i in range(1, len(music)):
    if music[i-1] - music[i] == -1:
        asc += 1
    elif music[i-1] - music[i] == 1:
        desc += 1
    else:
        mix += 1

if asc == 8:
    print("ascending")
elif desc == 8:
    print("descending")
else:
    print("mixed")