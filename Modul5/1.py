class Mahasiswa(object):
    def __init__(self,nama,nim,kota,us):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = us

class MhsTIF (Mahasiswa):  
    def katakanPy(self):
        print('Python is cool.')
        
listan = [MhsTIF ('Veny',45,'Sukoharjo', 150000),
MhsTIF('Vara',46,'Surakarta', 900000),
MhsTIF('Najwa',51,'Yogyakarta', 123000),
MhsTIF('Siska',38,'Boyolali', 130000),
MhsTIF('Yana',31,'Pekalongan', 25000),
MhsTIF('Zua',30,'Magelang', 980000),
MhsTIF('Dewi',33,'Semarang', 269000),
MhsTIF('Dhinda',24,'Surabaya', 112000),
MhsTIF('Nadine',21,'Cikarang', 575000),
MhsTIF('Meimei',26,'Bogor', 22000),
MhsTIF('Niken',100,'Jakarta', 135000)]

#1
def urutkannim(l):
    n = len(l)
    for i in range (n -1) :
        for k in range (n-i-1) :
            if l[k].nim > l[k+1].nim :
                swap(l,k,k+1)

def checknimdong (l):
    for i in l :
        print (i.nim)

def swap (a, p, q) :
    tmp = a[p]
    a[p] = a[q]
    a[q] = tmp
