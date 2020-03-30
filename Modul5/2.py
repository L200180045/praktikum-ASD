def mengurutkan(A,B):
    C = A+B
    n = len(C)
    for i in range(1,n):
        nilai=C[i]
        pos=i
        while pos > 0 and nilai < C[pos-1]:
            C[pos]=c[pos-1]
            pos=pos-1
        C[pos] = nilai
    return C
A = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
B = [21, 22, 23, 24, 25]
