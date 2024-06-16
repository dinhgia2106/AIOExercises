def levenshtein_distance(source, target):
    M = len(source)
    N = len(target)
    D = [[0] * (N + 1) for _ in range(M + 1)]

    for i in range(1, M + 1):
        n = i - 1
        D[i][0] = source[n]
    for j in range(1, N + 1):
        k = j - 1
        D[0][j] = target[k]

    print(D)


source = "yu"
target = "you"
distance = levenshtein_distance(source, target)
