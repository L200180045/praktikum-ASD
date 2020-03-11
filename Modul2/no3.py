class manusia(object):
    keadaan = "lapar"
    def __init__(self,nama):
        self.nama = nama
    def ucapkansalam(self):
        print("salam, namaku", self.nama)

class mahasiswa(manusia):
    def __init__(self,nama,nim,kota,us):
        self.nama = nama
        self.nim = nim
        self.kota = kota
        self.uangsaku = us
    def __str__(self):
        s = ' Nama: '+str(self.nama) + "" +', Nim : '+str(self.nim)+ "" +', kota : '+self.kota+ "" +', uang saku : '+self.uangsaku+' /bulan'
        return s

a = input("nama :")
b= input("nim :")
c = input("kota :")
d = input("uang saku per bulan :")
x = mahasiswa(a,b,c,d)
print("data mahasiswa :",x)
