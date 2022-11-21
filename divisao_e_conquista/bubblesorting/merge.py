def merge(splitted):
    merged = []

    for i in range(len(splitted) - 1):
        k = 0
        j = 0
        while (k < len(splitted[i + 1]) or j < len(splitted[i])):
            if (splitted[i][j] < splitted[i + 1][k]):
                merged += [splitted[i][j]]
                j += 1

            elif (splitted[i][j] > splitted[i + 1][k]):
                merged += [splitted[i + 1][k]]
                k += 1

            elif (splitted[i][j] > splitted[i + 1][k]):
                merged += [splitted[i][j]]
                k += 1
                j += 1

    return merged