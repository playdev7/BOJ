x = int(input())
files = []
f_name = ""
file1 = ""
file2 = ""
result = []

for i in range(x):
    f_name = input()
    files.append(f_name)
    if files[i-1] != files[i]:
        file1 = files[i]
        file2 = files[i-1]
        for j in range(len(file1)):
            if file1[j] == file2[j]:
                result.append(file2[j])
            else:
                result.append("?")

print("".join(result))