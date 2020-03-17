k = [[4,7],[4,4]]
l = [[5,6],[7,8]]
m = [[1,3,9,9],[2,"x",4]]
n = [[3,24],[32,5],[31,5]]
o = [[2,3,3],[17,2,22]]
p = [[8,9,20],[1,2,3],[3,4,5]]

## 1a ##
def cekKonsisten(n):
    x = len(n[0])
    z = 0
    for i in range(len(n)):
        if (len(n[i]) == x):
           z+=1
    if(z == len(n)):
        print("matriks konsisten")
    else:
        print("matrik tidak konsisten")
print("##NOMOR 1a")
cekKonsisten(k)
cekKonsisten(l)
cekKonsisten(m)

def cekInteger(n):
    x = 0
    y = 0
    for i in n:
        for j in i:
            y+=1
            if (str(j).isdigit()==False):
                print("tidak semua isi matriks adalah angka")
                break
            else:
                x+=1
    if(x==y):
        print("semua isi matriks adalah angka")
        
cekInteger(k)
cekInteger(l)
cekInteger(m)

## 1b ##
def cekordo(n):
    x,y = 0,0
    for i in range(len(n)):
        x+=1
        y = len(n[i])
    print("mempunyai ordo "+str(x)+"x"+str(y))

print("##NOMOR 1b")
cekordo(k)
cekordo(l)
cekordo(m)
cekordo(n)

## 1c ##
def jumlah(n,m):
    x,y = 0,0
    for i in range(len(n)):
        x+=1
        y = len(n[i])
    xy = [[0 for j in range(x)] for i in range(y)]
    
    z = 0
    if(len(n)==len(m)):
        for i in range(len(n)):
            if(len(n[i]) == len(m[i])):
                z+=1
    if(z==len(n) and z==len(m)):
        print("ukuran sama")
        for i in range(len(n)):
            for j in range(len(n[i])):
                xy[i][j] = n[i][j] + m[i][j]
        print(xy)
    else:
        print("ukuran beda")
        
print("##NOMOR 1c")
jumlah(k,l)
jumlah(k,n)
   
## 1d ##     
def kali(n,m):
    aa = 0
    x,y = 0,0
    for i in range(len(n)):
        x+=1
        y = len(n[i])
    v,w = 0,0
    for i in range(len(m)):
        v+=1
        w = len(m[i])
        
    if(y==v):
        print("bisa dikalikan")
        vwxy = [[0 for j in range(w)] for i in range(x)]
        for i in range(len(n)):
            for j in range(len(m[0])):
                for k in range(len(m)):
                    #print(n[i][k], m[k][j])
                    vwxy[i][j] += n[i][k] * m[k][j]
        print(vwxy)
            
    else:
        print("tidak memenuhi syarat")
print("##NOMOR 1d")
zz = [[1,2,3],[1,2,3]]
zx = [[1],[2],[3]]
kali(zz,zx)
kali(k,l)
kali(k,o)
kali(k,zx)

## 1e ##
def determinanHitung(A, total=0):
    x = len(A[0])
    z = 0
    for i in range(len(A)):
        if (len(A[i]) == x):
           z+=1
    if(z == len(A)):
        if(x==len(A)):
            indices = list(range(len(A)))
            if len(A) == 2 and len(A[0]) == 2:
                val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
                return val
            for fc in indices: 
                As = A 
                As = As[1:] 
                height = len(As) 
                for i in range(height): 
                    As[i] = As[i][0:fc] + As[i][fc+1:] 
                sign = (-1) ** (fc % 2) 
                sub_det = determinanHitung(As)
                total += sign * A[0][fc] * sub_det
        else:
            return "tidak bisa dihitung determinannya, karena bukan matrix bujursangkar"
    else:
        return "tidak bisa dihitung determinannya, karena bukan matrix bujursangkar"
    return total


q = [[3,1],[2,5]]
r = [[1,2,1],[3,3,1],[2,1,2]]
s = [[1,-2,0,0],[3,2,-3,1],[4,0,5,1],[2,3,-1,4]]
t = [[10,23,45,12,13],[1,2,3,4,5],[1,2,3,4,6],[4,2,3,4,8],[1,4,5,6,10]]

print("##NOMOR 1e")
print(determinanHitung(q))
print(determinanHitung(r))
print(determinanHitung(s))
print(determinanHitung(t))
print(determinanHitung(n))
print(determinanHitung(o))
