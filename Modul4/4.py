class MhsTIF(object):
    def __init__(self, nama, nim, kota, uangsaku):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = uangsaku


class buatArray(object):
    internalData = 11 * [None]

    def __getitem__(self, item):
        return self.internalData[item]

    def __setitem__(self, key, value):
        self.internalData[key] = value

    def kurang250rb(self):
        d = []
        for i in self:
            if i.uangSaku < 250000:
                d.append((i.nama, i.nim, i.kotaTinggal, i.uangSaku))
        return d


c = buatArray()
c[0] = MhsTIF('Veny', 10, 'Sukoharjo', 245000)
c[1] = MhsTIF('Vara', 51, 'Solo', 215000)
c[2] = MhsTIF('Aulia', 2, 'Wonogiri', 245000)
c[3] = MhsTIF('Fannisa', 18, 'Magelang', 210000)
c[4] = MhsTIF('Vian', 4, 'Wonogiri', 260000)
c[5] = MhsTIF('Diul', 31, 'Sragen', 265000)
c[6] = MhsTIF('Salma', 10, 'Jepara', 240000)
c[7] = MhsTIF('Rina', 5, 'Boyolali', 230000)
c[8] = MhsTIF('Fitri', 64, 'Gemolong', 235000)
c[9] = MhsTIF('Ismi', 23, 'Polokarto', 245000)
c[10] = MhsTIF('Amy', 29, 'Klaten', 250000)
