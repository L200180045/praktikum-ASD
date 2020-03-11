class pesan(object):
    def __init__(self,a):
        self.a = a
    def apakahterkandung(self, b):
        return b in self.a
    def hitungkonsonan(self):
        itung = 0
        vokal = ["a","i","u","e","o","A","I","U","E","O"]
        for i in self.a:
            if i not in vokal:
                itung+=1
        return itung
    def hitungvokal(self):
        itung = 0
        vokal = ["a","i","u","e","o","A","I","U","E","O"]
        for i in self.a:
            if i in vokal:
                itung+=1
        return itung
