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
        s = self.nama + "" +'Nim'+str(self.nim)+ "" +'kota'+self.kota+ "" +'uang saku'+self.uangsaku+'/bulan'
        return s
    def ambilnama(self):
        return self.nama
    def ambilnim(self):
        return self.nim
    def ambilkotatinggal(self):
        return self.kota
    def ambiluangsaku(self):
        return self.uangsaku
    def perbaruikotatinggal(self,b):
        self.kota=b
    def tambahuangsaku(self,c):
        self.uangsaku+=c

