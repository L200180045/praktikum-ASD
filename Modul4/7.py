def binSe(kumpulan, target):
    low = 0
    high = len(kumpulan) - 1
    listku = []

    while low <= high:
        if kumpulan[low] == target:
            listku.append(low)
            low += 1
        else:
            low += 1
    return listku
