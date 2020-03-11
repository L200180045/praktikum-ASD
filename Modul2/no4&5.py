class manusia(object):
    keadaan = "lapar"
    def __init__(self,nama):
        self.nama = nama
    def ucapkansalam(self):
        print("salam, namaku", self.nama)

class mahasiswa(manusia):
    def __init__(self,nama,nim,kota,us,lk=[]):
        self.nama = nama
        self.nim = nim
        self.kota = kota
        self.uangsaku = us
        self.lk = lk
    def __str__(self):
        s = self.nama + ',Nim'+str(self.nim)+',kota'+self.kota+',uang saku'+self.uangsaku+'/bulan'
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

    def listkuliah(self):
        return self.lk
    def ambilkuliah(self,b):
        self.lk.append(b)

    def hapusmatakuliah(self,d):
        for x in self.lk:
            if d in self.lk:
                self.lk.remove(d)
            else:
                print("maaf anda tidak dapat menghapus matkul tersebut karena matkul tersebut tidak ada")


