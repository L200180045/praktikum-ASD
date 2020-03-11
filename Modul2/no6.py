from datetime import date
class manusia(object):
    keadaan = "lapar"
    def __init__(self,nama):
        self.nama = nama
    def ucapkansalam(self):
        print("salam, namaku", self.nama)


class SiswaSMA(manusia):
    def __init__(self, nama, nis, umur, us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.nis = nis
        self.umur = umur
        self.us = us
        
    def __str__(self):
        s = ' Nama ' +str(self.nama) +' NIS '+str(self.nis)\
            +'. Berumur '+ str(self.umur) \
            +'. Uang saku Rp. '+ str(self.us)\
            +' tiap harinya.'
        return s
    def ambilnama(self):
        return self.nama
    def ambilnim(self):
        return self.nis
    def ambilumur(self):
        return self.umur
    def ambiluangsaku(self):
        return self.us

    def tahunlahir(self):
        thnskr = date.today().year
        tl = thnskr - self.umur
        return tl
