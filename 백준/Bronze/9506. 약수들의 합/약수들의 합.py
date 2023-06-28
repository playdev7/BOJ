answer = list()
while True:
    T = int(input())
    if T == -1:
        break
    measures = list()
    for i in range(1, T):
        if T % i == 0:
            measures.append(i)
    else:
        if sum(measures) == T:
            print(f"{T} = {' + '.join([str(i) for i in measures])}")
        else:
            print(f"{T} is NOT perfect.")